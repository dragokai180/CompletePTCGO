"""Basic Energy is a verified step of the normal cbrew installation."""
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from spirit.tools import ptcgo_local_assets as installer


class CbrewEnergyInstallationTests(unittest.TestCase):
    def run_install(self, flags=(), failures=()):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory)
            with patch("sys.argv", ["installer", "--source", directory, *flags]), \
                 patch.object(installer, "import_card_art", return_value={
                     "written": 0, "unchanged": 0, "unavailable": 0,
                 }) as cards, \
                 patch.object(installer, "import_ui_bundles", return_value={
                     "bundles": 0, "written": 0, "unchanged": 0,
                 }) as menus, \
                 patch.object(installer, "seed_original_landing_pages", return_value=0), \
                 patch("spirit.tools.install_recent_card_art.install_native_energy",
                       return_value=list(failures)) as energies:
                result = installer.main()
                return result, source, cards, menus, energies

    def test_default_installs_energy_from_selected_source(self):
        result, source, cards, menus, energies = self.run_install()
        self.assertEqual(result, 0)
        cards.assert_called_once_with(source)
        menus.assert_called_once_with(source)
        energies.assert_called_once_with(False, str(source))

    def test_cards_only_includes_energy_without_menu_changes(self):
        result, source, cards, menus, energies = self.run_install(["--cards-only"])
        self.assertEqual(result, 0)
        energies.assert_called_once_with(False, str(source))
        menus.assert_not_called()

    def test_ui_only_does_not_install_or_check_energy(self):
        result, source, cards, menus, energies = self.run_install(["--ui-only"])
        self.assertEqual(result, 0)
        cards.assert_not_called()
        energies.assert_not_called()

    def test_missing_energy_is_not_silent_success(self):
        result, _, _, menus, energies = self.run_install(
            failures=["SWSH_Energy/FireEnergy_2: original texture unavailable"])
        self.assertEqual(result, 2)
        energies.assert_called_once()
        menus.assert_called_once()

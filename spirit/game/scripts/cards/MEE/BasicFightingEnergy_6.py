"""Regular Mega Evolution Energy printing."""
from uuid import NAMESPACE_URL, uuid5

from spirit.game.data_utils import reprint
from spirit.game.scripts.cards.SVE.BasicFightingEnergy_6 import card as base_card

card = reprint(
    base_card,
    guid=str(uuid5(NAMESPACE_URL, "completeptcgo:MEE:6")),
    set_code="MEE",
    key="MEE",
    collector_number=6,
    regulation_mark=None,
)

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.energies import capture_on_attach

card = EnergyCardDef(
    guid="40417df0-ec7f-5d30-90a8-6123062625b4",
    key="SWSH3",
    name="Capture Energy",
    display_name="Capture Energy",
    searchable_by=["Capture Energy", "Special"],
    subtypes=["Special"],
    collector_number=201,
    set_code="SWSH3",
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    on_attach=capture_on_attach,
)

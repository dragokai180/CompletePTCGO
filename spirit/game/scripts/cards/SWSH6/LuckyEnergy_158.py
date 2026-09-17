from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.energies import LuckyEnergyPassive

card = EnergyCardDef(
    guid="e66efd6e-a8c3-5233-aa0a-11c17f1fe25f",
    key="SWSH6",
    name="Lucky Energy",
    display_name="Lucky Energy",
    searchable_by=["Lucky Energy", "Special"],
    subtypes=["Special"],
    collector_number=158,
    set_code="SWSH6",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    outside_play_types=[],
    passive=LuckyEnergyPassive(),
)

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import attack_effect_shield_passive

card = EnergyCardDef(
    guid="7930ae70-22ad-536f-89fe-d66e203df5ec",
    key="SV05",
    name="Mist Energy",
    display_name="Mist Energy",
    searchable_by=["Mist Energy", "Special"],
    subtypes=["Special"],
    collector_number=161,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    passive=attack_effect_shield_passive(),
)

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import attack_effect_shield_passive

card = EnergyCardDef(
    guid="611d1f76-0535-5826-bcbc-c62ec7d3a89b",
    key="ME3",
    name="Rocky Fighting Energy",
    display_name="Rocky Fighting Energy",
    searchable_by=["Rocky Fighting Energy", "Special", "RockyFightingEnergy"],
    subtypes=["Special"],
    collector_number=87,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.FIGHTING,
    is_special=True,
    passive=attack_effect_shield_passive(pokemon_type=PokemonTypes.FIGHTING),
)

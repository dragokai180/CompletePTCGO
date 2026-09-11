from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid="9768ba4c-0a6e-5ade-9d27-d9a92d44b03b",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AncientBoosterEnergyCapsule.Name",
    display_name="Ancient Booster Energy Capsule",
    searchable_by=["Ancient Booster Energy Capsule", "Pokémon Tool", "Ancient", "AncientBoosterEnergyCapsule"],
    subtypes=["Pokémon Tool", "Ancient"],
    collector_number=140,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    passive=standard_passive("The Ancient Pokémon this card is attached to gets +60 HP, recovers from all Special Conditions, and can't be affected by any Special Conditions."),
)

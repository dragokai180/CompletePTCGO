from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid="26ce9eed-2c87-5aac-8c4d-308d00cac054",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FutureBoosterEnergyCapsule.Name",
    display_name="Future Booster Energy Capsule",
    searchable_by=["Future Booster Energy Capsule", "Pokémon Tool", "Future", "FutureBoosterEnergyCapsule"],
    subtypes=["Pokémon Tool", "Future"],
    collector_number=149,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    passive=standard_passive("The Future Pokémon this card is attached to has no Retreat Cost, and the attacks it uses do 20 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance)."),
)

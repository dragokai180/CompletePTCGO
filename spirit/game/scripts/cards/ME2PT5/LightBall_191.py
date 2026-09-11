from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid="44d6411a-7ebc-54b5-b590-8ce237cc822b",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LightBall.Name",
    display_name="Light Ball",
    searchable_by=["Light Ball", "Pokémon Tool", "LightBall"],
    subtypes=["Pokémon Tool"],
    collector_number=191,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    passive=standard_passive("Attacks used by the Pikachu ex this card is attached to do 50 more damage to your opponent's Active Pokémon ex (before applying Weakness and Resistance)."),
)

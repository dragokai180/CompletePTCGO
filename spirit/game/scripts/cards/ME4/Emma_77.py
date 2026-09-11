from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = SupporterCardDef(
    guid="d7c4d16f-2937-5457-bcf7-b4914a0fd7ea",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Emma.Name",
    display_name="Emma",
    searchable_by=["Emma", "Supporter", "Emma"],
    subtypes=["Supporter"],
    collector_number=77,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Your opponent reveals their hand, and you draw a card for each Pokémon you find there."),
)

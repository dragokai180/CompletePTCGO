from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = SupporterCardDef(
    guid="7d9ddd5d-b625-5f1f-9442-92b0d67da15e",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Naveen.Name",
    display_name="Naveen",
    searchable_by=["Naveen", "Supporter", "Naveen"],
    subtypes=["Supporter"],
    collector_number=79,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Draw cards until you have 5 cards in your hand. Before drawing cards, you may discard any number of cards from your hand. (If you can't draw any cards in this way, you can't use this card.)"),
)

from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='aa3d3ea1-bbe9-52c8-bd17-edbd6e89b18c',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Kahili.Name',
    display_name='Kahili',
    searchable_by=['Kahili', 'Supporter', 'Kahili'],
    subtypes=['Supporter'],
    collector_number=179,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Draw 2 cards. Then, flip a coin. If heads, if you played this Kahili from your hand, put this card into your hand instead of the discard pile. If you have no cards in your deck, you can't play this card."),
    condition=standard_trainer_condition("Draw 2 cards. Then, flip a coin. If heads, if you played this Kahili from your hand, put this card into your hand instead of the discard pile. If you have no cards in your deck, you can't play this card."),
)

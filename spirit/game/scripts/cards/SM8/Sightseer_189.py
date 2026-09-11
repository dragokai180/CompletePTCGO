from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='ed9c6b83-624d-5988-8e78-05bc8da629d2',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Sightseer.Name',
    display_name='Sightseer',
    searchable_by=['Sightseer', 'Supporter', 'Sightseer'],
    subtypes=['Supporter'],
    collector_number=189,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("You may discard any number of cards from your hand. Then, draw cards until you have 5 cards in your hand. If you can't draw any cards in this way, you can't play this card."),
    condition=standard_trainer_condition("You may discard any number of cards from your hand. Then, draw cards until you have 5 cards in your hand. If you can't draw any cards in this way, you can't play this card."),
)

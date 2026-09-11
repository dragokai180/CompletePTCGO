from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='1c654575-c481-5dce-aabf-0f3142da2fc0',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.trainer.TVReporter.Name',
    display_name='TV Reporter',
    searchable_by=['TV Reporter', 'Supporter', 'TVReporter'],
    subtypes=['Supporter'],
    collector_number=149,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Draw 3 cards. Then, discard a card from your hand. If you have no cards in your deck, you can't play this card."),
    condition=standard_trainer_condition("Draw 3 cards. Then, discard a card from your hand. If you have no cards in your deck, you can't play this card."),
)

from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='5b24b989-b802-57e1-b96b-4912c7be9eb4',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Clay.Name',
    display_name='Clay',
    searchable_by=['Clay', 'Supporter', 'Clay'],
    subtypes=['Supporter'],
    collector_number=188,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Discard the top 7 cards of your deck. If any of those cards are Item cards, put them into your hand.'),
    condition=standard_trainer_condition('Discard the top 7 cards of your deck. If any of those cards are Item cards, put them into your hand.'),
)

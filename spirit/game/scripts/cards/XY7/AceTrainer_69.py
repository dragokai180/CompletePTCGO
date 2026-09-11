from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='a1cdecf5-5c0e-5f3c-bf0f-16e31db744d8',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.trainer.AceTrainer.Name',
    display_name='Ace Trainer',
    searchable_by=['Ace Trainer', 'Supporter', 'AceTrainer'],
    subtypes=['Supporter'],
    collector_number=69,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('You can play this card only if you have more Prize cards left than your opponent. Each player shuffles his or her hand into his or her deck. Then, draw 6 cards. Your opponent draws 3 cards.'),
    condition=standard_trainer_condition('You can play this card only if you have more Prize cards left than your opponent. Each player shuffles his or her hand into his or her deck. Then, draw 6 cards. Your opponent draws 3 cards.'),
)

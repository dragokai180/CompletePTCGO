from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='33528646-2ab5-5dab-91c5-b0f7610b8d5c',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.trainer.CrasherWake.Name',
    display_name='Crasher Wake',
    searchable_by=['Crasher Wake', 'Supporter', 'CrasherWake'],
    subtypes=['Supporter'],
    collector_number=104,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Discard 2 Water Energy cards from your hand. If you do, search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck.'),
    condition=standard_trainer_condition('Discard 2 Water Energy cards from your hand. If you do, search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck.'),
)

from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='ee3235b0-c395-5758-8120-17fb8babec2e',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Rika.Name',
    display_name='Rika',
    searchable_by=['Rika', 'Supporter', 'Rika'],
    subtypes=['Supporter'],
    collector_number=172,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Look at the top 4 cards of your deck and put 2 of them into your hand. Shuffle the other cards and put them on the bottom of your deck.'),
    condition=standard_trainer_condition('Look at the top 4 cards of your deck and put 2 of them into your hand. Shuffle the other cards and put them on the bottom of your deck.'),
)

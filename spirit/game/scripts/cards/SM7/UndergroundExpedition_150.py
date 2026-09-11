from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='8e14809a-ab53-554a-8897-7c48c6b2b730',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.trainer.UndergroundExpedition.Name',
    display_name='Underground Expedition',
    searchable_by=['Underground Expedition', 'Supporter', 'UndergroundExpedition'],
    subtypes=['Supporter'],
    collector_number=150,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Look at the bottom 4 cards of your deck and put 2 of them into your hand. Put the other cards back on the bottom of your deck in any order.'),
    condition=standard_trainer_condition('Look at the bottom 4 cards of your deck and put 2 of them into your hand. Put the other cards back on the bottom of your deck in any order.'),
)

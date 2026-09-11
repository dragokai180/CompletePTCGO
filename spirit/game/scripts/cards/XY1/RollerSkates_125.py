from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='762c8466-bfbb-5e0b-ab40-00861f03ed81',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.RollerSkates.Name',
    display_name='Roller Skates',
    searchable_by=['Roller Skates', 'Item', 'RollerSkates'],
    subtypes=['Item'],
    collector_number=125,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Flip a coin. If heads, draw 3 cards. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Flip a coin. If heads, draw 3 cards. You may play as many Item cards as you like during your turn (before your attack).'),
)

from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='798bfab3-56f4-5135-ae07-45ae52e24f7e',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.trainer.LostBlender.Name',
    display_name='Lost Blender',
    searchable_by=['Lost Blender', 'Item', 'LostBlender'],
    subtypes=['Item'],
    collector_number=181,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Put 2 cards from your hand in the Lost Zone. If you do, draw a card. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Put 2 cards from your hand in the Lost Zone. If you do, draw a card. You may play as many Item cards as you like during your turn (before your attack).'),
)

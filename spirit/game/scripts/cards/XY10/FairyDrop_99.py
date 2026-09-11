from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='1442d11a-2ff6-55a7-b23e-c7b37dc4fc0c',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.trainer.FairyDrop.Name',
    display_name='Fairy Drop',
    searchable_by=['Fairy Drop', 'Item', 'FairyDrop'],
    subtypes=['Item'],
    collector_number=99,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Heal 50 damage from 1 of your Pokémon that has any Fairy Energy attached to it. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Heal 50 damage from 1 of your Pokémon that has any Fairy Energy attached to it. You may play as many Item cards as you like during your turn (before your attack).'),
)

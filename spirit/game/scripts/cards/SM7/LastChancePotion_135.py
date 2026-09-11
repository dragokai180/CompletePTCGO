from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='ae195811-c19a-598c-97b5-c879564382f6',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.trainer.LastChancePotion.Name',
    display_name='Last Chance Potion',
    searchable_by=['Last Chance Potion', 'Item', 'LastChancePotion'],
    subtypes=['Item'],
    collector_number=135,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Heal 120 damage from 1 of your Pokémon that has 30 HP or less remaining. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Heal 120 damage from 1 of your Pokémon that has 30 HP or less remaining. You may play as many Item cards as you like during your turn (before your attack).'),
)

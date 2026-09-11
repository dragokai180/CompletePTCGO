from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='5595381a-0377-5a0c-99aa-3bcec45efb8f',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.trainer.GreatPotion.Name',
    display_name='Great Potion',
    searchable_by=['Great Potion', 'Item', 'GreatPotion'],
    subtypes=['Item'],
    collector_number=198,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Heal 50 damage from your Active Pokémon-GX. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Heal 50 damage from your Active Pokémon-GX. You may play as many Item cards as you like during your turn (before your attack).'),
)

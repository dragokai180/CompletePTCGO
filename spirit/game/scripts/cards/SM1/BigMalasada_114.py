from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='7a2c3aff-ac27-5a97-8ca0-7e239c97e5ee',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.BigMalasada.Name',
    display_name='Big Malasada',
    searchable_by=['Big Malasada', 'Item', 'BigMalasada'],
    subtypes=['Item'],
    collector_number=114,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Heal 20 damage and remove a Special Condition from your Active Pokémon. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Heal 20 damage and remove a Special Condition from your Active Pokémon. You may play as many Item cards as you like during your turn (before your attack).'),
)

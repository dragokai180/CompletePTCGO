from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='61b59328-f41d-5248-b72a-c0fd4ed8217d',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.trainer.MixedHerbs.Name',
    display_name='Mixed Herbs',
    searchable_by=['Mixed Herbs', 'Item', 'MixedHerbs'],
    subtypes=['Item'],
    collector_number=184,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('You may play 2 Mixed Herbs cards at once.\n• If you played 1 card, remove a Special Condition from your Active Pokémon.\n• If you played 2 cards, heal 90 damage and remove all Special Conditions from your Active Pokémon. (This effects works one time for 2 cards.) You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('You may play 2 Mixed Herbs cards at once.\n• If you played 1 card, remove a Special Condition from your Active Pokémon.\n• If you played 2 cards, heal 90 damage and remove all Special Conditions from your Active Pokémon. (This effects works one time for 2 cards.) You may play as many Item cards as you like during your turn (before your attack).'),
)

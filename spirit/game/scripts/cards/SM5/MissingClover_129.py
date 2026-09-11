from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='f4f75452-c5dd-52c5-bc11-0c8d9522f3bd',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.trainer.MissingClover.Name',
    display_name='Missing Clover',
    searchable_by=['Missing Clover', 'Item', 'MissingClover'],
    subtypes=['Item'],
    collector_number=129,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('You may play 4 Missing Clover cards at once.\n• If you played 1 card, look at the top card of your deck.\n• If you played 4 cards, take a Prize card. (This effect works one time for 4 cards.) You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('You may play 4 Missing Clover cards at once.\n• If you played 1 card, look at the top card of your deck.\n• If you played 4 cards, take a Prize card. (This effect works one time for 4 cards.) You may play as many Item cards as you like during your turn (before your attack).'),
)

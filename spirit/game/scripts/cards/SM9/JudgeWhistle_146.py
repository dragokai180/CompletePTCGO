from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='ad58126a-a0ae-58e9-a4ec-db600586365d',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.trainer.JudgeWhistle.Name',
    display_name='Judge Whistle',
    searchable_by=['Judge Whistle', 'Item', 'JudgeWhistle'],
    subtypes=['Item'],
    collector_number=146,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Choose 1:\n• Draw a card\n• Put a Judge card from your discard pile into your hand. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Choose 1:\n• Draw a card\n• Put a Judge card from your discard pile into your hand. You may play as many Item cards as you like during your turn (before your attack).'),
)

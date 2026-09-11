from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='c60ee87a-7414-5475-ab8f-29dfa49dd9bb',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.trainer.ReturnLabel.Name',
    display_name='Return Label',
    searchable_by=['Return Label', 'Item', 'ReturnLabel'],
    subtypes=['Item'],
    collector_number=153,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Put a card from your opponent's discard pile on the bottom of their deck. You may play as many Item cards as you like during your turn (before your attack)."),
    condition=standard_trainer_condition("Put a card from your opponent's discard pile on the bottom of their deck. You may play as many Item cards as you like during your turn (before your attack)."),
)

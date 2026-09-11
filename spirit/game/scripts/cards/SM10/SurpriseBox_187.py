from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='9c5d0692-2693-5f40-8d83-cdc30271655c',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.trainer.SurpriseBox.Name',
    display_name='Surprise Box',
    searchable_by=['Surprise Box', 'Item', 'SurpriseBox'],
    subtypes=['Item'],
    collector_number=187,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Put a card from your opponent's discard pile into their hand. You may play as many Item cards as you like during your turn (before your attack)."),
    condition=standard_trainer_condition("Put a card from your opponent's discard pile into their hand. You may play as many Item cards as you like during your turn (before your attack)."),
)

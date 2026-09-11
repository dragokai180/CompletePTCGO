from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='06f9d510-ef03-5437-b9bd-5f1e0cfa3d77',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.trainer.ChipChipIceAxe.Name',
    display_name='Chip-Chip Ice Axe',
    searchable_by=['Chip-Chip Ice Axe', 'Item', 'ChipChipIceAxe'],
    subtypes=['Item'],
    collector_number=165,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Look at the top 3 cards of your opponent's deck and choose 1 of them. Your opponent shuffles the other cards back into their deck. Then, put the card you chose on top of their deck. You may play as many Item cards as you like during your turn (before your attack)."),
    condition=standard_trainer_condition("Look at the top 3 cards of your opponent's deck and choose 1 of them. Your opponent shuffles the other cards back into their deck. Then, put the card you chose on top of their deck. You may play as many Item cards as you like during your turn (before your attack)."),
)

from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='710d6432-b23e-5aa0-bfdf-56071c6bf6b3',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.trainer.FireCrystal.Name',
    display_name='Fire Crystal',
    searchable_by=['Fire Crystal', 'Item', 'FireCrystal'],
    subtypes=['Item'],
    collector_number=173,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Put 3 Fire Energy cards from your discard pile into your hand. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Put 3 Fire Energy cards from your discard pile into your hand. You may play as many Item cards as you like during your turn (before your attack).'),
)

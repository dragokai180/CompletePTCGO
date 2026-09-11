from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='59cde074-a448-5463-ab52-40a51cb0c9c3',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.trainer.ArmorFossilShieldon.Name',
    display_name='Armor Fossil Shieldon',
    searchable_by=['Armor Fossil Shieldon', 'Item', 'ArmorFossilShieldon'],
    subtypes=['Item'],
    collector_number=98,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Look at the bottom 7 cards of your deck. You may reveal a Shieldon you find there and put it onto your Bench. Shuffle the other cards back into your deck. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Look at the bottom 7 cards of your deck. You may reveal a Shieldon you find there and put it onto your Bench. Shuffle the other cards back into your deck. You may play as many Item cards as you like during your turn (before your attack).'),
)

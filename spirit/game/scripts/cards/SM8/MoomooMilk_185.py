from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='18c207d0-88ff-551a-a391-add93b936b6d',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.trainer.MoomooMilk.Name',
    display_name='Moomoo Milk',
    searchable_by=['Moomoo Milk', 'Item', 'MoomooMilk'],
    subtypes=['Item'],
    collector_number=185,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Choose 1 of your Pokémon, and then flip 2 coins. For each heads, heal 30 damage from that Pokémon. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Choose 1 of your Pokémon, and then flip 2 coins. For each heads, heal 30 damage from that Pokémon. You may play as many Item cards as you like during your turn (before your attack).'),
)

from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='0c698d08-3e32-57c7-b9ef-f490af9b53e7',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.trainer.MultiSwitch.Name',
    display_name='Multi Switch',
    searchable_by=['Multi Switch', 'Item', 'MultiSwitch'],
    subtypes=['Item'],
    collector_number=129,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Move an Energy from 1 of your Benched Pokémon to your Active Pokémon. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Move an Energy from 1 of your Benched Pokémon to your Active Pokémon. You may play as many Item cards as you like during your turn (before your attack).'),
)

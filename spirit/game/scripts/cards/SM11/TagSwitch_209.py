from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='33950d93-fcd2-571b-b874-86f31f0ded2e',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.trainer.TagSwitch.Name',
    display_name='Tag Switch',
    searchable_by=['Tag Switch', 'Item', 'TagSwitch'],
    subtypes=['Item'],
    collector_number=209,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Move up to 2 Energy from 1 of your TAG TEAM Pokémon to another of your Pokémon. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Move up to 2 Energy from 1 of your TAG TEAM Pokémon to another of your Pokémon. You may play as many Item cards as you like during your turn (before your attack).'),
)

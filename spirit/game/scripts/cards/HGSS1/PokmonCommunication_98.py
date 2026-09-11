from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='591b3e73-8a9f-55ab-900c-9c42e842840c',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.PokmonCommunication.Name',
    display_name='Pokémon Communication',
    searchable_by=['Pokémon Communication', 'Item', 'PokmonCommunication'],
    subtypes=['Item'],
    collector_number=98,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Choose 1 Pokémon in your hand, show it to your opponent, and put it on top of your deck. If you do, search your deck for a Pokémon, show it to your opponent, and put it into your hand. Shuffle your deck afterward.'),
    condition=standard_trainer_condition('Choose 1 Pokémon in your hand, show it to your opponent, and put it on top of your deck. If you do, search your deck for a Pokémon, show it to your opponent, and put it into your hand. Shuffle your deck afterward.'),
)

from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='b7c58442-1e30-51b9-b283-f08a6b335f2e',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.ToolRetriever.Name',
    display_name='Tool Retriever',
    searchable_by=['Tool Retriever', 'Item', 'ToolRetriever'],
    subtypes=['Item'],
    collector_number=101,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Choose up to 2 Pokémon Tool cards attached to your Pokémon and put them into your hand. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Choose up to 2 Pokémon Tool cards attached to your Pokémon and put them into your hand. You may play as many Item cards as you like during your turn (before your attack).'),
)

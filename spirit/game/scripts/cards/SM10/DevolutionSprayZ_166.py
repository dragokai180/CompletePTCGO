from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='cd6aad16-2ac2-5568-a8d3-098477c3d15d',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.trainer.DevolutionSprayZ.Name',
    display_name='Devolution Spray Z',
    searchable_by=['Devolution Spray Z', 'Item', 'DevolutionSprayZ'],
    subtypes=['Item'],
    collector_number=166,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Devolve 1 of your evolved Pokémon by shuffling any number of Evolution cards on it into your deck. (That Pokémon can't evolve this turn.) You may play as many Item cards as you like during your turn (before your attack)."),
    condition=standard_trainer_condition("Devolve 1 of your evolved Pokémon by shuffling any number of Evolution cards on it into your deck. (That Pokémon can't evolve this turn.) You may play as many Item cards as you like during your turn (before your attack)."),
)

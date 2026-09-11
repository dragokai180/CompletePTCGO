from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='180b57c2-e73c-5589-86fb-7242717055e6',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Evosoda.Name',
    display_name='Evosoda',
    searchable_by=['Evosoda', 'Item', 'Evosoda'],
    subtypes=['Item'],
    collector_number=116,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Search your deck for a card that evolves from 1 of your Pokémon and put it onto that Pokémon. (This counts as evolving that Pokémon.) Shuffle your deck afterward. You can't use this card during your first turn or on a Pokémon that was put into play this turn. You may play as many Item cards as you like during your turn (before your attack)."),
    condition=standard_trainer_condition("Search your deck for a card that evolves from 1 of your Pokémon and put it onto that Pokémon. (This counts as evolving that Pokémon.) Shuffle your deck afterward. You can't use this card during your first turn or on a Pokémon that was put into play this turn. You may play as many Item cards as you like during your turn (before your attack)."),
)

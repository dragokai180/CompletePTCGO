from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ed0be64c-c5c0-58ef-8f90-847e563c0c78',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Inkay.Name',
    display_name='Inkay',
    searchable_by=['Inkay', 'Basic', 'Inkay'],
    subtypes=['Basic'],
    collector_number=74,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=686,
    abilities=[
        Ability(
            title='Upside-Down Evolution',
            game_text='Once during your turn, (before your attack), if this Pokémon is Confused, you may search your deck for a card that evolves from this Pokémon and put it onto this Pokémon. (This counts as evolving this Pokémon.) Shuffle your deck afterward.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Confusion Wave',
            game_text='Both Active Pokémon are now Confused.',
            cost={PokemonTypes.DARKNESS: 1},
            effect=standard_attack,
        ),
    ],
)

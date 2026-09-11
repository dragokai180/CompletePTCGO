from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='68fbb567-1a34-5469-97cc-6cd11c4370cb',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.LugiaBREAK.Name',
    display_name='Lugia BREAK',
    searchable_by=['Lugia BREAK', 'BREAK', 'LugiaBREAK'],
    subtypes=['BREAK'],
    collector_number=79,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.BreakRare,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Lugia.Name',
    family_id=249,
    abilities=[
        Attack(
            title='Flash of Destruction',
            game_text='Discard 2 Energy attached to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 4},
            damage=150,
            effect=standard_attack,
        ),
    ],
)

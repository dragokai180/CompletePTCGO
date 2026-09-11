from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='10219225-a107-533d-b2cf-3cc00e6f65d6',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.PyroarBREAK.Name',
    display_name='Pyroar BREAK',
    searchable_by=['Pyroar BREAK', 'BREAK', 'PyroarBREAK'],
    subtypes=['BREAK'],
    collector_number=24,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.BreakRare,
    hp=160,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pyroar.Name',
    family_id=667,
    abilities=[
        Attack(
            title='Kaiser Tackle',
            game_text='This Pokémon does 50 damage to itself.',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=standard_attack,
        ),
    ],
)

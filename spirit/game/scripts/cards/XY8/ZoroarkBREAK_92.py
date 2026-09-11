from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='de2cdf48-d739-5183-b3fd-2ee9c600fb56',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.ZoroarkBREAK.Name',
    display_name='Zoroark BREAK',
    searchable_by=['Zoroark BREAK', 'BREAK', 'ZoroarkBREAK'],
    subtypes=['BREAK'],
    collector_number=92,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.BreakRare,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Zoroark.Name',
    family_id=570,
    abilities=[
        Attack(
            title='Foul Play',
            game_text="Choose 1 of your opponent's Active Pokémon's attacks and use it as this attack.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=standard_attack,
        ),
    ],
)

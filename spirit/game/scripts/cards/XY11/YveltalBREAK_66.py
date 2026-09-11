from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c8652a62-42ce-5693-a6f9-f2dae1b2824a',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.YveltalBREAK.Name',
    display_name='Yveltal BREAK',
    searchable_by=['Yveltal BREAK', 'BREAK', 'YveltalBREAK'],
    subtypes=['BREAK'],
    collector_number=66,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.BreakRare,
    hp=150,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Yveltal.Name',
    family_id=717,
    abilities=[
        Attack(
            title='Baleful Night',
            game_text="This attack does 30 damage to each of your opponent's Benched Pokémon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.DARKNESS: 3},
            damage=120,
            effect=standard_attack,
        ),
    ],
)

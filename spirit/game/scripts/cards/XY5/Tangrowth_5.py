from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6949fc15-103e-5628-826e-d72479c0ed7d',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tangrowth.Name',
    display_name='Tangrowth',
    searchable_by=['Tangrowth', 'Stage 1', 'Tangrowth'],
    subtypes=['Stage 1'],
    collector_number=5,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tangela.Name',
    family_id=114,
    abilities=[
        Attack(
            title='Mega Drain',
            game_text='Heal 20 damage from this Pokémon.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=standard_attack,
        ),
        Attack(
            title='Grass Knot',
            game_text="This attack does 10 more damage for each Colorless in your opponent's Active Pokémon's Retreat Cost.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

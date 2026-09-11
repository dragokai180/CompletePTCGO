from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c6b2a4ff-a602-540b-9fdf-ee401183f0ab',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Incineroar.Name',
    display_name='Incineroar',
    searchable_by=['Incineroar', 'Stage 2', 'Incineroar'],
    subtypes=['Stage 2'],
    collector_number=26,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Torracat.Name',
    family_id=725,
    abilities=[
        Attack(
            title='Fire Fang',
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Darkest Lariat',
            game_text='Flip 2 coins. This attack does 100 damage for each heads.',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)

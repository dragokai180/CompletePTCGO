from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='92075c7f-085e-5fd2-99d8-4b80674ac635',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dodrio.Name',
    display_name='Dodrio',
    searchable_by=['Dodrio', 'Stage 1', 'Dodrio'],
    subtypes=['Stage 1'],
    collector_number=117,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Doduo.Name',
    family_id=84,
    abilities=[
        Ability(
            title='Retreat Aid',
            game_text="As long as this Pokémon is on your Bench, your Active Pokémon's Retreat Cost is ColorlessColorless less.",
            passive=standard_passive("As long as this Pokémon is on your Bench, your Active Pokémon's Retreat Cost is ColorlessColorless less."),
        ),
        Attack(
            title='Fury Attack',
            game_text='Flip 3 coins. This attack does 40 damage times the number of heads.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)

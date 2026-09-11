from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1311e61f-4974-5f9b-b166-9776748d90c7',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cloyster.Name',
    display_name='Cloyster',
    searchable_by=['Cloyster', 'Stage 1', 'Cloyster'],
    subtypes=['Stage 1'],
    collector_number=32,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Shellder.Name',
    family_id=90,
    abilities=[
        Attack(
            title='Clamp Crush',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed and discard an Energy attached to that Pokémon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Spike Cannon',
            game_text='Flip 5 coins. This attack does 30 damage times the number of heads.',
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)

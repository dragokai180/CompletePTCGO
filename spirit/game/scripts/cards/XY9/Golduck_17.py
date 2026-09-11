from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='265e6bff-96a0-551c-ad73-37d074b3ad8f',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Golduck.Name',
    display_name='Golduck',
    searchable_by=['Golduck', 'Stage 1', 'Golduck'],
    subtypes=['Stage 1'],
    collector_number=17,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name',
    family_id=54,
    abilities=[
        Attack(
            title='Derail',
            game_text="Discard a Special Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Hydro Splash',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='58f46713-7c66-52ad-9049-0496e2899cab',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kingambit.Name',
    display_name='Kingambit',
    searchable_by=['Kingambit', 'Stage 2', 'Kingambit'],
    subtypes=['Stage 2'],
    collector_number=150,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=180,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Bisharp.Name',
    family_id=624,
    abilities=[
        Attack(
            title='Strike Down',
            game_text="If your opponent's Active Pokémon has 4 or more damage counters on it, that Pokémon is Knocked Out.",
            cost={PokemonTypes.METAL: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Massive Rend',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=140,
        ),
    ],
)

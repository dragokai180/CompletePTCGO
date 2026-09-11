from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2f6ab80d-a9c2-54fa-b380-e554ac7dcc1b',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.RaichuGX.Name',
    display_name='Raichu-GX',
    searchable_by=['Raichu-GX', 'Stage 1', 'GX', 'RaichuGX'],
    subtypes=['Stage 1', 'GX'],
    collector_number=90,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=210,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name',
    family_id=25,
    abilities=[
        Attack(
            title='Powerful Spark',
            game_text='This attack does 20 more damage times the amount of Lightning Energy attached to your Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Thunder',
            game_text='This Pokémon does 30 damage to itself.',
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=standard_attack,
        ),
        Attack(
            title='Voltail-GX',
            game_text="Your opponent's Active Pokémon is now Paralyzed. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
            gx=True,
        ),
    ],
)

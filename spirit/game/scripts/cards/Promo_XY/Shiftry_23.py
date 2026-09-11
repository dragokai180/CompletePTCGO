from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cc42f256-9d42-50e7-8186-1d6d90d7e61a',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Shiftry.Name',
    display_name='Shiftry',
    searchable_by=['Shiftry', 'Stage 2', 'Shiftry'],
    subtypes=['Stage 2'],
    collector_number=23,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Nuzleaf.Name',
    family_id=275,
    abilities=[
        Attack(
            title='Whisk Away',
            game_text="Your opponent reveals his or her hand. Choose a Pokémon you find there and put it on the bottom your opponent's deck. If you do, this attack does 30 more damage.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Spirit Dance',
            game_text='Flip 2 coins. This attack does 30 more damage for each heads.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

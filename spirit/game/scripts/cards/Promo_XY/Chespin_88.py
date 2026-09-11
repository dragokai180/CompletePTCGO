from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='44bdbcfa-0936-55e2-ae3d-769c6471d563',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Chespin.Name',
    display_name='Chespin',
    searchable_by=['Chespin', 'Basic', 'Chespin'],
    subtypes=['Basic'],
    collector_number=88,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=650,
    abilities=[
        Attack(
            title='Vine Whip',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5556b9a3-db89-5867-8a11-470365b2c17a',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Regigigas.Name',
    display_name='Regigigas',
    searchable_by=['Regigigas', 'Basic', 'Regigigas'],
    subtypes=['Basic'],
    collector_number=247,
    set_code='Promo_SWSH',
    regulation_mark='F',
    rarity=Rarities.RarePromo,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    attributes={200790: {'type': 'string', 'value': 'SWSH247'}},
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=486,
    abilities=[
        Attack(
            title='Limber Up',
            game_text='Attach a basic Energy card from your discard pile to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Double Impact',
            game_text='Flip 2 coins. This attack does 120 damage for each heads.',
            cost={PokemonTypes.COLORLESS: 4},
            damage=120,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)

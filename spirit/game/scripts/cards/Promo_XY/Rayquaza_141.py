from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8e10320d-08f4-5ccd-a0cc-99ebffb7694c',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Rayquaza.Name',
    display_name='Rayquaza',
    searchable_by=['Rayquaza', 'Basic', 'Rayquaza'],
    subtypes=['Basic'],
    collector_number=141,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=384,
    abilities=[
        Attack(
            title='Dual Claw',
            game_text='Flip 2 coins. This attack does 20 damage times the number of heads.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Dragon Blast',
            game_text='Discard 1 Fire Energy and 1 Lightning Energy attached to this Pokémon.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=standard_attack,
        ),
    ],
)

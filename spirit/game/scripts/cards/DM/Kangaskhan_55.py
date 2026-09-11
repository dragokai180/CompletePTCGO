from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9db6f2df-2e7a-5305-857e-387f02e87c2b',
    key='DM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kangaskhan.Name',
    display_name='Kangaskhan',
    searchable_by=['Kangaskhan', 'Basic', 'Kangaskhan'],
    subtypes=['Basic'],
    collector_number=55,
    set_code='DM',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=115,
    abilities=[
        Attack(
            title='Fetch',
            game_text='Draw a card.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Headbutt',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title='One-Two Punch',
            game_text='Flip a coin. If heads, this attack does 30 more damage.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

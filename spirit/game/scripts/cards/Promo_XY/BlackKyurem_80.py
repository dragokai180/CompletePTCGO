from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a8ef1f96-5925-50d6-a59d-562ddd65be75',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.BlackKyurem.Name',
    display_name='Black Kyurem',
    searchable_by=['Black Kyurem', 'Basic', 'BlackKyurem'],
    subtypes=['Basic'],
    collector_number=80,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=646,
    abilities=[
        Attack(
            title='Thunder Nail',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=standard_attack,
        ),
        Attack(
            title='Frozen Slice',
            game_text='This Pokémon does 20 damage to itself.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
        ),
    ],
)

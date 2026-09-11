from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e77c48f4-aa04-5e64-8fec-632fab591288',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.BlackKyurem.Name',
    display_name='Black Kyurem',
    searchable_by=['Black Kyurem', 'Basic', 'BlackKyurem'],
    subtypes=['Basic'],
    collector_number=160,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=646,
    abilities=[
        Attack(
            title='Ice Wing',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
        Attack(
            title='Frosty Thunder',
            game_text="If this Pokémon has any Lightning Energy attached to it, this attack does 20 damage to each of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=standard_attack,
        ),
    ],
)

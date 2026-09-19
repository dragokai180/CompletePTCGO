from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a2eda500-3d04-5e0c-b8ad-9a1e95cec501',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wooloo.Name',
    display_name='Wooloo',
    searchable_by=['Wooloo', 'Basic', 'Wooloo'],
    subtypes=['Basic'],
    collector_number=11,
    set_code='Promo_SWSH',
    regulation_mark='D',
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'SWSH011'}},
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=831,
    abilities=[
        Attack(
            title='Defense Curl',
            game_text="Flip a coin. If heads, prevent all damage done to this Pokémon by attacks during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Headbutt',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)

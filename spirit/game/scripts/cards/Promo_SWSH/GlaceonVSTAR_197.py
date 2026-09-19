from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)



card = PokemonCardDef(
    guid='484383e7-9e55-5875-b4ed-963853342850',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.GlaceonVSTAR.Name',
    display_name='Glaceon VSTAR',
    searchable_by=['Glaceon VSTAR', 'VSTAR', 'GlaceonVSTAR'],
    subtypes=['VSTAR'],
    collector_number=197,
    set_code='Promo_SWSH',
    regulation_mark='F',
    rarity=Rarities.RarePromo,
    hp=260,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    attributes={200790: {'type': 'string', 'value': 'SWSH197'}},
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.GlaceonV.Name',
    family_id=471,
    abilities=[
        Attack(
            title='Icicle Shot',
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=standard_attack,
        ),
        Attack(
            title='Crystal Star',
            game_text="During your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon. (You can't use more than 1 VSTAR Power in a game.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=220,
            effect=standard_attack,
            vstar=True,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='332eb702-5a3a-50e5-8019-1985de5ff803',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Leafeon.Name',
    display_name='Leafeon',
    searchable_by=['Leafeon', 'Stage 1', 'Leafeon'],
    subtypes=['Stage 1'],
    collector_number=191,
    set_code='Promo_SWSH',
    regulation_mark='E',
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'SWSH191'}},
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name',
    family_id=133,
    abilities=[
        Attack(
            title='Leaf Guard',
            game_text="During your opponent's next turn, this Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Grass Knot',
            game_text="This attack does 30 more damage for each Colorless in your opponent's Active Pokémon's Retreat Cost.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

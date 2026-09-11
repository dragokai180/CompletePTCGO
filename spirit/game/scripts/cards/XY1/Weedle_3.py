from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8fe73a37-91a0-521f-9feb-36df35f29a1b',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Weedle.Name',
    display_name='Weedle',
    searchable_by=['Weedle', 'Basic', 'Weedle'],
    subtypes=['Basic'],
    collector_number=3,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=13,
    abilities=[
        Attack(
            title='Leaf Munch',
            game_text="If your opponent's Active Pokémon is a Grass Pokémon, this attack does 20 more damage.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

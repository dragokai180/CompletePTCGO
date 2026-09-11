from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f941eef3-3ec3-520e-860c-f111f14f5d1f',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Skiddo.Name',
    display_name='Skiddo',
    searchable_by=['Skiddo', 'Basic', 'Skiddo'],
    subtypes=['Basic'],
    collector_number=16,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=672,
    abilities=[
        Attack(
            title='Razor Leaf',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
        Attack(
            title='Rising Lunge',
            game_text='Flip a coin. If heads, this attack does 20 more damage.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

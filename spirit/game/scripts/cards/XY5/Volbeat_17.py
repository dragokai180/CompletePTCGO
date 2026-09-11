from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c0bb20c9-daf2-564a-b549-813788b015ce',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Volbeat.Name',
    display_name='Volbeat',
    searchable_by=['Volbeat', 'Basic', 'Volbeat'],
    subtypes=['Basic'],
    collector_number=17,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=313,
    abilities=[
        Attack(
            title='Acrobatics',
            game_text='Flip 2 coins. This attack does 20 more damage for each heads.',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Pester',
            game_text="If your opponent's Active Pokémon is affected by a Special Condition, this attack does 30 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

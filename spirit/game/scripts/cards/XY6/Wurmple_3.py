from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='dd54191e-cb2f-57cd-8713-b2723ef7e275',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wurmple.Name',
    display_name='Wurmple',
    searchable_by=['Wurmple', 'Basic', 'Wurmple'],
    subtypes=['Basic'],
    collector_number=3,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=265,
    abilities=[
        Attack(
            title='Flock',
            game_text='Search your deck for Wurmple and put it onto your Bench. Shuffle your deck afterward.',
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Tackle',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)

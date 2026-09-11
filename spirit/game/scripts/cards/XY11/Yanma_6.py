from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0ceabf29-5d1f-54e1-a9fb-6b9dfa616ee4',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Yanma.Name',
    display_name='Yanma',
    searchable_by=['Yanma', 'Basic', 'Yanma'],
    subtypes=['Basic'],
    collector_number=6,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=193,
    abilities=[
        Attack(
            title='Scout',
            game_text='Your opponent reveals his or her hand.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Speed Dive',
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
        ),
    ],
)

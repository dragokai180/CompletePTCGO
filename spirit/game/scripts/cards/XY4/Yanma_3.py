from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c1256632-4307-5146-a4f3-05ff93e19753',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Yanma.Name',
    display_name='Yanma',
    searchable_by=['Yanma', 'Basic', 'Yanma'],
    subtypes=['Basic'],
    collector_number=3,
    set_code='XY4',
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
            title='Air Slash',
            game_text='Discard an Energy attached to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)

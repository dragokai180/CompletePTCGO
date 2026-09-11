from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='eadfb806-7ec6-564a-aaef-586e5c14d6ad',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Chinchou.Name',
    display_name='Chinchou',
    searchable_by=['Chinchou', 'Basic', 'Chinchou'],
    subtypes=['Basic'],
    collector_number=49,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=170,
    abilities=[
        Attack(
            title='Searching Light',
            game_text='Look at 1 of your face-down Prize cards.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Electro Ball',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e6cb9d3d-b7c9-5d03-aebc-11621dcc19f3',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Passimian.Name',
    display_name='Passimian',
    searchable_by=['Passimian', 'Basic', 'Passimian'],
    subtypes=['Basic'],
    collector_number=125,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=766,
    abilities=[
        Attack(
            title='Spike Draw',
            game_text='Draw 2 cards.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Seismic Toss',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)

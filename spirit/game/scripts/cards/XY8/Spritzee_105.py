from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4405fdab-73f5-55d6-8b1e-208644b7c78f',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Spritzee.Name',
    display_name='Spritzee',
    searchable_by=['Spritzee', 'Basic', 'Spritzee'],
    subtypes=['Basic'],
    collector_number=105,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=682,
    abilities=[
        Attack(
            title='Flail',
            game_text='This attack does 10 damage times the number of damage counters on this Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)

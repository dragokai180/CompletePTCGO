from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ec5ea4a5-0072-5c08-a98a-b5bd8746ed99',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Spritzee.Name',
    display_name='Spritzee',
    searchable_by=['Spritzee', 'Basic', 'Spritzee'],
    subtypes=['Basic'],
    collector_number=92,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
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
            title='Sweet Scent',
            game_text='Heal 20 damage from 1 of your Pokémon.',
            cost={PokemonTypes.FAIRY: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Flop',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)

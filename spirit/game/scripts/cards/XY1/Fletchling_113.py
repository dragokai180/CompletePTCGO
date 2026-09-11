from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f726b998-c9e7-59b1-935e-094cc7a4d32c',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Fletchling.Name',
    display_name='Fletchling',
    searchable_by=['Fletchling', 'Basic', 'Fletchling'],
    subtypes=['Basic'],
    collector_number=113,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=661,
    abilities=[
        Attack(
            title='Me First',
            game_text='Draw a card.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Peck',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)

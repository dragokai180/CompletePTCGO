from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e8939964-fa2e-5b7e-a57d-6d3e9606e378',
    key='DM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Swablu.Name',
    display_name='Swablu',
    searchable_by=['Swablu', 'Basic', 'Swablu'],
    subtypes=['Basic'],
    collector_number=56,
    set_code='DM',
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
    family_id=333,
    abilities=[
        Attack(
            title='Collect',
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

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9f83fb13-7494-5a63-afd3-32ac13a1c357',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Vullaby.Name',
    display_name='Vullaby',
    searchable_by=['Vullaby', 'Basic', 'Vullaby'],
    subtypes=['Basic'],
    collector_number=92,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=629,
    abilities=[
        Attack(
            title='Collect',
            game_text='Draw a card.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Corkscrew Punch',
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
    ],
)

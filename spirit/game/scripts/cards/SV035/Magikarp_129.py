from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='276c2d9e-e9bd-53b7-a791-6874c06047bf',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name',
    display_name='Magikarp',
    searchable_by=['Magikarp', 'Basic', 'Magikarp'],
    subtypes=['Basic'],
    collector_number=129,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=129,
    abilities=[
        Attack(
            title='Splashy Splash',
            game_text='Flip a coin until you get tails. For each heads, draw a card.',
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
    ],
)

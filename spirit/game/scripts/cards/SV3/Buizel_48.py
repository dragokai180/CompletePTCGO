from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2869285e-2fb8-5426-8a36-64ccce7bcc79',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Buizel.Name',
    display_name='Buizel',
    searchable_by=['Buizel', 'Basic', 'Buizel'],
    subtypes=['Basic'],
    collector_number=48,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=418,
    abilities=[
        Attack(
            title='Quick Attack',
            game_text='Flip a coin. If heads, this attack does 10 more damage.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

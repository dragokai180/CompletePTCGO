from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='227275a5-a7cb-591b-9401-555bf462ccbd',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Froakie.Name',
    display_name='Froakie',
    searchable_by=['Froakie', 'Basic', 'Froakie'],
    subtypes=['Basic'],
    collector_number=56,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=656,
    abilities=[
        Attack(
            title='Try Bouncing',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)

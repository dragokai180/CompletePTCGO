from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7564d13b-1800-54c7-b84f-8aadcbb1b4f6',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pineco.Name',
    display_name='Pineco',
    searchable_by=['Pineco', 'Basic', 'Pineco'],
    subtypes=['Basic'],
    collector_number=63,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=204,
    abilities=[
        Attack(
            title='Focus Energy',
            game_text="During your next turn, Pineco's Surprise Attack attack's base damage is 80.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Surprise Attack',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6b97ffd8-deed-5923-be4b-eab62a46a414',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Stunky.Name',
    display_name='Stunky',
    searchable_by=['Stunky', 'Basic', 'Stunky'],
    subtypes=['Basic'],
    collector_number=69,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=434,
    abilities=[
        Attack(
            title='Double Scratch',
            game_text='Flip 2 coins. This attack does 10 damage times the number of heads.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)

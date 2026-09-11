from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='61089f17-24e7-5fab-9a21-5743a2677756',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cetoddle.Name',
    display_name='Cetoddle',
    searchable_by=['Cetoddle', 'Basic', 'Cetoddle'],
    subtypes=['Basic'],
    collector_number=54,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=974,
    abilities=[
        Attack(
            title='Rest',
            game_text='This Pokémon is now Asleep. Heal 60 damage from it.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Double-Edge',
            game_text='This Pokémon also does 10 damage to itself.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=standard_attack,
        ),
    ],
)

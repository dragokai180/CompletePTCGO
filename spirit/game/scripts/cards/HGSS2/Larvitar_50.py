from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4e0a6f59-c4c9-5403-81d7-089e157a0023',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Larvitar.Name',
    display_name='Larvitar',
    searchable_by=['Larvitar', 'Basic', 'Larvitar'],
    subtypes=['Basic'],
    collector_number=50,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    family_id=246,
    abilities=[
        Attack(
            title='Mountain Eater',
            game_text="Discard the top card of your opponent's deck. Then, remove 2 damage counters from Larvitar.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Reckless Charge',
            game_text='Larvitar does 10 damage to itself.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)

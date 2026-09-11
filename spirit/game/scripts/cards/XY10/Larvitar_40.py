from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='80355ace-d21b-5300-a184-a7f610b98584',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Larvitar.Name',
    display_name='Larvitar',
    searchable_by=['Larvitar', 'Basic', 'Larvitar'],
    subtypes=['Basic'],
    collector_number=40,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=246,
    abilities=[
        Attack(
            title='Reckless Charge',
            game_text='This Pokémon does 10 damage to itself.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)

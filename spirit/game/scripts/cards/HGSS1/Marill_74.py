from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f62ee2ab-5c3b-54b8-aab7-fc09e4895554',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Marill.Name',
    display_name='Marill',
    searchable_by=['Marill', 'Basic', 'Marill'],
    subtypes=['Basic'],
    collector_number=74,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=183,
    abilities=[
        Attack(
            title='Water Splash',
            game_text='Flip a coin. If heads, this attack does 10 damage plus 10 more damage.',
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Tail Slap',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)

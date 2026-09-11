from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c9cc30f7-3f50-56b3-a2a2-96c3b74c5f3a',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name',
    display_name='Magikarp',
    searchable_by=['Magikarp', 'Basic', 'Magikarp'],
    subtypes=['Basic'],
    collector_number=72,
    set_code='HGSS1',
    regulation_mark=None,
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
            title='Splash',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)

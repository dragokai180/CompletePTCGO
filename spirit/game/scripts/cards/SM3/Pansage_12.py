from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='145c6dd3-66b0-512f-a62a-83b0212a537e',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pansage.Name',
    display_name='Pansage',
    searchable_by=['Pansage', 'Basic', 'Pansage'],
    subtypes=['Basic'],
    collector_number=12,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=511,
    abilities=[
        Attack(
            title='Vine Whip',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)

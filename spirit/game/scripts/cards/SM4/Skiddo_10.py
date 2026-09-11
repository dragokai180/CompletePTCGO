from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e0852e35-8bab-537b-9f2c-d2d13eb76d46',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Skiddo.Name',
    display_name='Skiddo',
    searchable_by=['Skiddo', 'Basic', 'Skiddo'],
    subtypes=['Basic'],
    collector_number=10,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=672,
    abilities=[
        Attack(
            title='Seed Bomb',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)

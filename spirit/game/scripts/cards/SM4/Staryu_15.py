from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2cbc4b4f-7039-541a-94a2-d55f2cb8bd3a',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name',
    display_name='Staryu',
    searchable_by=['Staryu', 'Basic', 'Staryu'],
    subtypes=['Basic'],
    collector_number=15,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=120,
    abilities=[
        Attack(
            title='Spinning Attack',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d35a77d6-bc1d-5317-9f6e-00ef398b8021',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mudkip.Name',
    display_name='Mudkip',
    searchable_by=['Mudkip', 'Basic', 'Mudkip'],
    subtypes=['Basic'],
    collector_number=33,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=258,
    abilities=[
        Attack(
            title='Tackle',
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title='Mud-Slap',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)

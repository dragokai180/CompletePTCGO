from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bd1c829a-885c-54b9-b4ad-93faeae1c1c1',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Diglett.Name',
    display_name='Diglett',
    searchable_by=['Diglett', 'Basic', 'Diglett'],
    subtypes=['Basic'],
    collector_number=50,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=50,
    abilities=[
        Attack(
            title='Headbutt Bounce',
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
        Attack(
            title='Mud-Slap',
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
        ),
    ],
)

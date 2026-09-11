from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a026b978-b32b-52b7-8fea-d07b6268e04f',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Spheal.Name',
    display_name='Spheal',
    searchable_by=['Spheal', 'Basic', 'Spheal'],
    subtypes=['Basic'],
    collector_number=49,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=363,
    abilities=[
        Attack(
            title='Rollout',
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title='Icy Snow',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b7397c6e-098c-5f91-997a-08685d7c6b74',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Spheal.Name',
    display_name='Spheal',
    searchable_by=['Spheal', 'Basic', 'Spheal'],
    subtypes=['Basic'],
    collector_number=24,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=363,
    abilities=[
        Attack(
            title='Ice Ball',
            cost={PokemonTypes.WATER: 2},
            damage=20,
        ),
    ],
)

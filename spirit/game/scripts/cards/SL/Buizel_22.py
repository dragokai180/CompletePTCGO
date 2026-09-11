from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1b6eb21f-46fa-5331-a5e8-c0a655b41a40',
    key='SL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Buizel.Name',
    display_name='Buizel',
    searchable_by=['Buizel', 'Basic', 'Buizel'],
    subtypes=['Basic'],
    collector_number=22,
    set_code='SL',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=418,
    abilities=[
        Attack(
            title='Razor Fin',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Water Gun',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)

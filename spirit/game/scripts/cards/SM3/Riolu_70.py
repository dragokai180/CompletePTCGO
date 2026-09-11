from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='09c8317a-06e5-5330-b459-dbc03cd8ac3b',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name',
    display_name='Riolu',
    searchable_by=['Riolu', 'Basic', 'Riolu'],
    subtypes=['Basic'],
    collector_number=70,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=447,
    abilities=[
        Attack(
            title='Punch',
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
        Attack(
            title='Low Kick',
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
        ),
    ],
)

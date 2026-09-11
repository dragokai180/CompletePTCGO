from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e9682687-f570-5d0c-9cb4-1f12dcbbe00d',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Totodile.Name',
    display_name='Totodile',
    searchable_by=['Totodile', 'Basic', 'Totodile'],
    subtypes=['Basic'],
    collector_number=86,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=158,
    abilities=[
        Attack(
            title='Gnaw',
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title='Wave Splash',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1c25554f-f782-57e7-964b-db9335abd3eb',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Charcadet.Name',
    display_name='Charcadet',
    searchable_by=['Charcadet', 'Basic', 'Charcadet'],
    subtypes=['Basic'],
    collector_number=43,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=935,
    abilities=[
        Attack(
            title='Light Punch',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Combustion',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)

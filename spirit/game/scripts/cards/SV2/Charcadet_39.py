from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0a4ebd1e-8a96-52e6-a6bc-060c0714119f',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Charcadet.Name',
    display_name='Charcadet',
    searchable_by=['Charcadet', 'Basic', 'Charcadet'],
    subtypes=['Basic'],
    collector_number=39,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=935,
    abilities=[
        Attack(
            title='Live Coal',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Magnum Punch',
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
    ],
)

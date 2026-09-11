from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a0975787-fbbf-58a9-84c6-4016a80a1cc1',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Charcadet.Name',
    display_name='Charcadet',
    searchable_by=['Charcadet', 'Basic', 'Charcadet'],
    subtypes=['Basic'],
    collector_number=38,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=935,
    abilities=[
        Attack(
            title='Kick',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)

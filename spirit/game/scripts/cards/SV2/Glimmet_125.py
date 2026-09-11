from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bb60da25-bedc-5e20-aa37-bd4d313349bd',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Glimmet.Name',
    display_name='Glimmet',
    searchable_by=['Glimmet', 'Basic', 'Glimmet'],
    subtypes=['Basic'],
    collector_number=125,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=969,
    abilities=[
        Attack(
            title='Rock Throw',
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9a522962-cdc2-5e4f-b8d3-df17ca29db84',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Noibat.Name',
    display_name='Noibat',
    searchable_by=['Noibat', 'Basic', 'Noibat'],
    subtypes=['Basic'],
    collector_number=152,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=714,
    abilities=[
        Attack(
            title='Gust',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1},
            damage=40,
        ),
    ],
)

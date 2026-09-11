from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7c86f6c9-1b2f-5dd6-935d-d218212ddff8',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Croagunk.Name',
    display_name='Croagunk',
    searchable_by=['Croagunk', 'Basic', 'Croagunk'],
    subtypes=['Basic'],
    collector_number=130,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=453,
    abilities=[
        Attack(
            title='Beat',
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
        Attack(
            title='Whap Down',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)

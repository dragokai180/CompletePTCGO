from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8f7b508d-d90c-5522-8735-0ae7dafad63f',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tepig.Name',
    display_name='Tepig',
    searchable_by=['Tepig', 'Basic', 'Tepig'],
    subtypes=['Basic'],
    collector_number=31,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=498,
    abilities=[
        Attack(
            title='Live Coal',
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
        Attack(
            title='Rollout',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4e0c3597-2356-5b5b-a52a-0fd8afff9771',
    key='XY0',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bidoof.Name',
    display_name='Bidoof',
    searchable_by=['Bidoof', 'Basic', 'Bidoof'],
    subtypes=['Basic'],
    collector_number=29,
    set_code='XY0',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=399,
    abilities=[
        Attack(
            title='Rollout',
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
    ],
)

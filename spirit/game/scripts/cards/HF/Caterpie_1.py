from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='429ef5b5-4997-545b-abf9-be38f40d76d8',
    key='HF',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Caterpie.Name',
    display_name='Caterpie',
    searchable_by=['Caterpie', 'Basic', 'Caterpie'],
    subtypes=['Basic'],
    collector_number=1,
    set_code='HF',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=10,
    abilities=[
        Attack(
            title='Tackle',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)

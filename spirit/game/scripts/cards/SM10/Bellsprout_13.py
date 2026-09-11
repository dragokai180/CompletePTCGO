from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='88f7bd23-71ef-5e83-92bc-9728e9658cc4',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bellsprout.Name',
    display_name='Bellsprout',
    searchable_by=['Bellsprout', 'Basic', 'Bellsprout'],
    subtypes=['Basic'],
    collector_number=13,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=69,
    abilities=[
        Attack(
            title='Razor Leaf',
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e08c61ba-a476-5b9d-b33d-c298112f8bf2',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Surskit.Name',
    display_name='Surskit',
    searchable_by=['Surskit', 'Basic', 'Surskit'],
    subtypes=['Basic'],
    collector_number=13,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=283,
    abilities=[
        Attack(
            title='Stampede',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)

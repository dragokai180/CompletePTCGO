from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ce8af9a3-044e-5e0e-942d-aedf050fab4e',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Stufful.Name',
    display_name='Stufful',
    searchable_by=['Stufful', 'Basic', 'Stufful'],
    subtypes=['Basic'],
    collector_number=111,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=759,
    abilities=[
        Attack(
            title='Tackle',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)

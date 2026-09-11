from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7bc338f9-8af0-5ae6-8d3b-f41c755b1cfb',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cherubi.Name',
    display_name='Cherubi',
    searchable_by=['Cherubi', 'Basic', 'Cherubi'],
    subtypes=['Basic'],
    collector_number=47,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    family_id=420,
    abilities=[
        Attack(
            title='Tackle',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)

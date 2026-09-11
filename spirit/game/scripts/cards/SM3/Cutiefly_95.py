from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e145dfdc-7f76-539e-8196-d7ea335d3c65',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cutiefly.Name',
    display_name='Cutiefly',
    searchable_by=['Cutiefly', 'Basic', 'Cutiefly'],
    subtypes=['Basic'],
    collector_number=95,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=742,
    abilities=[
        Attack(
            title='Fairy Wind',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)

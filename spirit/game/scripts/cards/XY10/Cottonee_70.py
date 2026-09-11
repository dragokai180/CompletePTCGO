from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1073e7d3-98aa-5f92-9453-e6735f5c0548',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cottonee.Name',
    display_name='Cottonee',
    searchable_by=['Cottonee', 'Basic', 'Cottonee'],
    subtypes=['Basic'],
    collector_number=70,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=546,
    abilities=[
        Attack(
            title='Fairy Wind',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)

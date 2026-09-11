from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='784b9e12-82c9-59ed-9c1c-ae7ba57d2bac',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name',
    display_name='Exeggcute',
    searchable_by=['Exeggcute', 'Basic', 'Exeggcute'],
    subtypes=['Basic'],
    collector_number=1,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=102,
    abilities=[
        Attack(
            title='Multiply',
            game_text='Search your deck for Exeggcute and put it onto your Bench. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)

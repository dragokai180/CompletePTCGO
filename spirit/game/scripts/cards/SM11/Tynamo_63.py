from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='07b7014f-6783-5a6f-9c76-876e9d07c6d2',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tynamo.Name',
    display_name='Tynamo',
    searchable_by=['Tynamo', 'Basic', 'Tynamo'],
    subtypes=['Basic'],
    collector_number=63,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=602,
    abilities=[
        Attack(
            title='Wild River',
            game_text='Switch this Pokémon with 1 of your Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)

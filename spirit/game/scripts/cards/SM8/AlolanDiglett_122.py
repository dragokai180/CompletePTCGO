from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bb1a524e-209d-5f39-8bb6-0a5da77611d4',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanDiglett.Name',
    display_name='Alolan Diglett',
    searchable_by=['Alolan Diglett', 'Basic', 'AlolanDiglett'],
    subtypes=['Basic'],
    collector_number=122,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=50,
    abilities=[
        Attack(
            title='Call for Family',
            game_text='Search your deck for a Basic Pokémon and put it onto your Bench. Then, shuffle your deck.',
            cost={},
            effect=standard_attack,
        ),
    ],
)

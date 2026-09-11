from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='10c5dcf6-9783-5ea3-b881-764f138bc74b',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Litwick.Name',
    display_name='Litwick',
    searchable_by=['Litwick', 'Basic', 'Litwick'],
    subtypes=['Basic'],
    collector_number=48,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=607,
    abilities=[
        Attack(
            title='Slightly Simmer',
            game_text='Search your deck for up to 2 cards and discard them. Shuffle your deck afterward.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)

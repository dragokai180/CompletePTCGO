from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ba9bd381-05db-5a6a-b366-4c494d7887cd',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Minccino.Name',
    display_name='Minccino',
    searchable_by=['Minccino', 'Basic', 'Minccino'],
    subtypes=['Basic'],
    collector_number=86,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=572,
    abilities=[
        Attack(
            title='Cleaning Up',
            game_text="Discard a Pokémon Tool card attached to 1 of your opponent's Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)

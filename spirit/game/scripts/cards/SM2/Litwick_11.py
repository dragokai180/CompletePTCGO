from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='684234e5-c85e-5a7e-ae02-8a1133485736',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Litwick.Name',
    display_name='Litwick',
    searchable_by=['Litwick', 'Basic', 'Litwick'],
    subtypes=['Basic'],
    collector_number=11,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=607,
    abilities=[
        Attack(
            title='Flickering Flames',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)

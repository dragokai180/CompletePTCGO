from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1d6d8c40-932f-589b-936a-b0cad186113a',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gible.Name',
    display_name='Gible',
    searchable_by=['Gible', 'Basic', 'Gible'],
    subtypes=['Basic'],
    collector_number=96,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=443,
    abilities=[
        Attack(
            title='Ascension',
            game_text='Search your deck for a card that evolves from this Pokémon and put it onto this Pokémon to evolve it. Then, shuffle your deck.',
            cost={PokemonTypes.FIGHTING: 1},
            effect=standard_attack,
        ),
    ],
)

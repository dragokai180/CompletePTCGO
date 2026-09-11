from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b850b6dc-c7ae-5d88-81b4-9ecd394541f2',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gastly.Name',
    display_name='Gastly',
    searchable_by=['Gastly', 'Basic', 'Gastly'],
    subtypes=['Basic'],
    collector_number=67,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=92,
    abilities=[
        Ability(
            title='Swelling Spite',
            game_text='When this Pokémon is Knocked Out, search your deck for up to 2 Haunter and put them onto your Bench. Then, shuffle your deck.',
            effect=standard_ability,
            trigger=Triggers.ON_KNOCKED_OUT,
        ),
        Attack(
            title='Will-O-Wisp',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)

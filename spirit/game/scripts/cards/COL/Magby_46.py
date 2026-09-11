from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5c6bdbb5-7ef6-5861-8758-b4293fd296a0',
    key='COL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Magby.Name',
    display_name='Magby',
    searchable_by=['Magby', 'Basic', 'Magby'],
    subtypes=['Basic'],
    collector_number=46,
    set_code='COL',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=30,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=240,
    abilities=[
        Ability(
            title='Sweet Sleeping Face',
            game_text='As long as Magby is Asleep, prevent all damage done to Magby by attacks.',
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive('As long as Magby is Asleep, prevent all damage done to Magby by attacks.'),
        ),
        Attack(
            title='Play with Fire',
            game_text='The Defending Pokémon is now Burned. Magby is now Asleep.',
            cost={},
            effect=standard_attack,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d9c8bc79-bede-562b-9e9f-e31ee5d8979e',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Magby.Name',
    display_name='Magby',
    searchable_by=['Magby', 'Basic', 'Magby'],
    subtypes=['Basic'],
    collector_number=41,
    set_code='HGSS4',
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
            game_text='As long as Magby is Asleep, prevents all damage done to Magby by attacks.',
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive('As long as Magby is Asleep, prevents all damage done to Magby by attacks.'),
        ),
        Attack(
            title='Play with Fire',
            game_text='The Defending Pokémon is now Burned. Magby is now Asleep.',
            cost={},
            effect=standard_attack,
        ),
    ],
)

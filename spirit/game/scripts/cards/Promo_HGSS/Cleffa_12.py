from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='46603c27-5db2-577f-ba3c-11467787bae8',
    key='Promo_HGSS',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cleffa.Name',
    display_name='Cleffa',
    searchable_by=['Cleffa', 'Basic', 'Cleffa'],
    subtypes=['Basic'],
    collector_number=12,
    set_code='Promo_HGSS',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=30,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    attributes={200790: {'type': 'string', 'value': 'HGSS12'}},
    family_id=173,
    abilities=[
        Ability(
            title='Sweet Sleeping Face',
            game_text='As long as Cleffa is Asleep, prevent all damage done to Cleffa by attacks.',
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive('As long as Cleffa is Asleep, prevent all damage done to Cleffa by attacks.'),
        ),
        Attack(
            title='Eeeeeeek',
            game_text='Shuffle your hand into your deck, then draw 6 cards. Cleffa is now Asleep.',
            cost={},
            effect=standard_attack,
        ),
    ],
)

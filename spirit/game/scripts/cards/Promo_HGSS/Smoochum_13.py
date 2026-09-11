from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='82535574-9cf4-5102-a22b-50359067e382',
    key='Promo_HGSS',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Smoochum.Name',
    display_name='Smoochum',
    searchable_by=['Smoochum', 'Basic', 'Smoochum'],
    subtypes=['Basic'],
    collector_number=13,
    set_code='Promo_HGSS',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    attributes={200790: {'type': 'string', 'value': 'HGSS13'}},
    family_id=238,
    abilities=[
        Ability(
            title='Sweet Sleeping Face',
            game_text='As long as Smoochum is Asleep, prevent all damage done to Smoochum by attacks.',
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive('As long as Smoochum is Asleep, prevent all damage done to Smoochum by attacks.'),
        ),
        Attack(
            title='Energy Antics',
            game_text="Move an Energy card attached to 1 of your opponent's Pokémon to another of your opponent's Pokémon. Smoochum is now Asleep.",
            cost={},
            effect=standard_attack,
        ),
    ],
)

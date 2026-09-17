from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e6d8942b-f349-5d4d-904a-317f4f775aa7',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ditto.Name',
    display_name='Ditto',
    searchable_by=['Ditto', 'Basic', 'Ditto'],
    subtypes=['Basic'],
    collector_number=115,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=132,
    abilities=[
        Attack(
            title='Surprisingly Transform',
            game_text='Flip a coin. If heads, search your deck for a Pokémon and switch it with this Pokémon. Any attached cards, damage counters, Special Conditions, turns in play, and any other effects remain on the new Pokémon. If you switched a Pokémon in this way, put this card into your deck. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cd854dc3-c455-5a99-94b7-7b4b708084de',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Xerneas.Name',
    display_name='Xerneas',
    searchable_by=['Xerneas', 'Basic', 'Xerneas'],
    subtypes=['Basic'],
    collector_number=76,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=716,
    abilities=[
        Attack(
            title='Geonavigation',
            game_text='Search your deck for up to 2 Stadium cards, reveal them, and put them into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Aurora Horns',
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)

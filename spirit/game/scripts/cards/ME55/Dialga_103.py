from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1c799dc9-9f5a-57b1-af84-4eab2568a342',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dialga.Name',
    display_name='Dialga',
    searchable_by=['Dialga', 'Basic', 'Dialga'],
    subtypes=['Basic'],
    collector_number=103,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=483,
    abilities=[
        Attack(
            title='Reversed Clock',
            game_text='Shuffle up to 3 in any combination of Pokémon and Basic Energy cards from your discard pile into your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Heavy Impact',
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)

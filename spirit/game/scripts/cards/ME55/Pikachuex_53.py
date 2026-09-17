from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='75ecfdb6-aab7-5656-a3f2-f2977cb91cf0',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pikachuex.Name',
    display_name='Pikachu ex',
    searchable_by=['Pikachu ex', 'Basic', 'ex', 'Pikachuex'],
    subtypes=['Basic', 'ex'],
    collector_number=53,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.RareHoloEX,
    hp=190,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=25,
    abilities=[
        Attack(
            title='Pika-Pika Parade',
            game_text='Search your deck for any number of Basic Pokémon and put them onto your Bench. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Thunderbolt',
            game_text='Discard all Energy from this Pokémon.',
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)

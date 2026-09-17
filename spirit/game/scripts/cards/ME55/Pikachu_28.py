from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='08151883-f747-5df4-9a41-965903eabe8e',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name',
    display_name='Pikachu',
    searchable_by=['Pikachu', 'Basic', 'Pikachu'],
    subtypes=['Basic'],
    collector_number=28,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=25,
    abilities=[
        Ability(
            title='Lonely Gaze',
            game_text="As long as this Pokémon is in the Active Spot, attacks used by your opponent's Active Pokémon do 20 less damage (before applying Weakness and Resistance).",
            passive=standard_passive("As long as this Pokémon is in the Active Spot, attacks used by your opponent's Active Pokémon do 20 less damage (before applying Weakness and Resistance)."),
        ),
        Attack(
            title='Pika Ball',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)

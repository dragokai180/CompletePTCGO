from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0d4f071a-3819-53f6-9aa3-b1dc8131a04a',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.FlyingPikachu.Name',
    display_name='Flying Pikachu',
    searchable_by=['Flying Pikachu', 'Basic', 'FlyingPikachu'],
    subtypes=['Basic'],
    collector_number=110,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.RareSecret,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=25,
    abilities=[
        Attack(
            title='Thunder Shock',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            effect=standard_attack,
        ),
        Attack(
            title='Fly',
            game_text="Flip a coin. If tails, this attack does nothing. If heads, prevent all effects of attacks, including damage, done to this Pokémon during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            effect=standard_attack,
        ),
    ],
)

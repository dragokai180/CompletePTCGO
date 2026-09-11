from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5d41d6e0-2b07-5d37-a10f-1111d66b83ea',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Electabuzz.Name',
    display_name='Electabuzz',
    searchable_by=['Electabuzz', 'Basic', 'Electabuzz'],
    subtypes=['Basic'],
    collector_number=41,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=125,
    abilities=[
        Attack(
            title='Thunder Shock',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            effect=standard_attack,
        ),
        Attack(
            title='Thunder Punch',
            game_text='Flip a coin. If heads, this attack does 10 more damage. If tails, this Pokémon does 10 damage to itself.',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

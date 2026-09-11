from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1e3298b3-dd68-53f7-9d01-f7c14dd94940',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Squawkabilly.Name',
    display_name='Squawkabilly',
    searchable_by=['Squawkabilly', 'Basic', 'Squawkabilly'],
    subtypes=['Basic'],
    collector_number=162,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=931,
    abilities=[
        Attack(
            title='Call for Family',
            game_text='Search your deck for up to 2 Basic Pokémon and put them onto your Bench. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Fly',
            game_text="Flip a coin. If tails, this attack does nothing. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)

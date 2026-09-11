from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a9d82a14-800f-5f02-9e78-f969af42cdfa',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Snorlax.Name',
    display_name='Snorlax',
    searchable_by=['Snorlax', 'Basic', 'Snorlax'],
    subtypes=['Basic'],
    collector_number=80,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=143,
    abilities=[
        Ability(
            title='Stir and Snooze',
            game_text='If this Pokémon is Asleep, flip 2 coins instead of 1 between turns. If either of them is tails, this Pokémon is still Asleep.',
            effect=standard_ability,
            trigger=Triggers.BETWEEN_TURNS,
        ),
        Attack(
            title='Sleepy Press',
            game_text='Heal 20 damage from this Pokémon. This Pokémon is now Asleep.',
            cost={PokemonTypes.COLORLESS: 4},
            damage=120,
            effect=standard_attack,
        ),
    ],
)

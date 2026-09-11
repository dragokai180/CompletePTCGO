from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='18f3c85f-22a4-5834-905b-806c5a373074',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Slaking.Name',
    display_name='Slaking',
    searchable_by=['Slaking', 'Stage 2', 'Slaking'],
    subtypes=['Stage 2'],
    collector_number=162,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Vigoroth.Name',
    family_id=287,
    abilities=[
        Ability(
            title='Stir and Snooze',
            game_text='If this Pokémon is Asleep, flip 2 coins instead of 1 during Pokémon Checkup. If either of them is tails, this Pokémon is still Asleep.',
            effect=standard_ability,
            trigger=Triggers.BETWEEN_TURNS,
        ),
        Attack(
            title="Slacker's Headstrike",
            game_text='This Pokémon is now Asleep.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=240,
            effect=standard_attack,
        ),
    ],
)

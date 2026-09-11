from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='407ce2d8-ce50-5543-a1bb-7c4d89ade0bf',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Darkrai.Name',
    display_name='Darkrai ◇',
    searchable_by=['Darkrai ◇', 'Basic', 'Prism Star', 'Darkrai'],
    subtypes=['Basic', 'Prism Star'],
    collector_number=77,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Prism,
    hp=160,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=491,
    abilities=[
        Ability(
            title='Nightmare Star',
            game_text='When you play this Pokémon from your hand onto your Bench during your turn, you may attach 2 Darkness Energy cards from your hand to it.',
            effect=standard_ability,
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title='Abyssal Sleep',
            game_text="Your opponent's Active Pokémon is now Asleep. Your opponent flips 2 coins instead of 1 between turns. If either of them is tails, that Pokémon is still Asleep.",
            cost={PokemonTypes.DARKNESS: 4},
            damage=120,
            effect=standard_attack,
        ),
    ],
)

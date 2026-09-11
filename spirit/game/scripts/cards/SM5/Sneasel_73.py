from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ea678464-7edc-5785-8fcb-f3767294d4bd',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sneasel.Name',
    display_name='Sneasel',
    searchable_by=['Sneasel', 'Basic', 'Sneasel'],
    subtypes=['Basic'],
    collector_number=73,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=215,
    abilities=[
        Attack(
            title='Sneaky Smash',
            game_text="You can use this attack only if you go second, and only on your first turn. Discard an Energy from 1 of your opponent's Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Ambush',
            game_text='Flip a coin. If heads, this attack does 20 more damage.',
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

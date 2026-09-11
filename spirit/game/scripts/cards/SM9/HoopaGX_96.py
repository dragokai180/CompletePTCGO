from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6f696557-513d-50de-a317-db6e3bae8921',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.HoopaGX.Name',
    display_name='Hoopa-GX',
    searchable_by=['Hoopa-GX', 'Basic', 'GX', 'HoopaGX'],
    subtypes=['Basic', 'GX'],
    collector_number=96,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=190,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=720,
    abilities=[
        Attack(
            title='Rogue Ring',
            game_text='Search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.DARKNESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Dark Strike',
            game_text="This Pokémon can't use Dark Strike during your next turn.",
            cost={PokemonTypes.DARKNESS: 3},
            damage=160,
            effect=standard_attack,
            locks_next_turn=True,
        ),
        Attack(
            title='Devilish Hands-GX',
            game_text="Choose 1 of your opponent's Pokémon-GX or Pokémon-EX 6 times. (You can choose the same Pokémon more than once.) For each time you chose a Pokémon, do 30 damage to it. This damage isn't affected by Weakness or Resistance. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.DARKNESS: 3},
            effect=standard_attack,
            gx=True,
        ),
    ],
)

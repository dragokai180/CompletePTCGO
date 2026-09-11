from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1078c2ac-187a-5a51-8092-f80a33af7601',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Xerneas.Name',
    display_name='Xerneas ◇',
    searchable_by=['Xerneas ◇', 'Basic', 'Prism Star', 'Xerneas'],
    subtypes=['Basic', 'Prism Star'],
    collector_number=144,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Prism,
    hp=160,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=716,
    abilities=[
        Ability(
            title='Path of Life',
            game_text='Once during your turn, when this Pokémon moves from your Bench to become your Active Pokémon, you may move any number of Energy from your other Pokémon to it.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Bright Horns',
            game_text="This Pokémon can't use Bright Horns during your next turn.",
            cost={PokemonTypes.FAIRY: 3},
            damage=160,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)

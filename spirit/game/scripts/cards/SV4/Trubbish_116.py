from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e7ef6cec-0020-59e5-bf73-d3d06c0dbb73',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Trubbish.Name',
    display_name='Trubbish',
    searchable_by=['Trubbish', 'Basic', 'Trubbish'],
    subtypes=['Basic'],
    collector_number=116,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=568,
    abilities=[
        Attack(
            title='Suffocating Gas',
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
        Attack(
            title='Venomous Hit',
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)

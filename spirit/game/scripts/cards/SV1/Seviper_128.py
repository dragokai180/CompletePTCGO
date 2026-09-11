from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='efa748b9-cb35-5e80-b6b4-86d09e291562',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Seviper.Name',
    display_name='Seviper',
    searchable_by=['Seviper', 'Basic', 'Seviper'],
    subtypes=['Basic'],
    collector_number=128,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=336,
    abilities=[
        Attack(
            title='Spit Poison',
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Venoshock',
            game_text="If your opponent's Active Pokémon is Poisoned, this attack does 120 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

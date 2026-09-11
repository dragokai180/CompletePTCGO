from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8c70b4a6-de8e-500b-b4c7-6c123b985fd0',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Liepard.Name',
    display_name='Liepard',
    searchable_by=['Liepard', 'Stage 1', 'Liepard'],
    subtypes=['Stage 1'],
    collector_number=57,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Purrloin.Name',
    family_id=509,
    abilities=[
        Attack(
            title='Gentle Bite',
            game_text="During your opponent's next turn, any damage done by attacks from the Defending Pokémon is reduced by 60 (before applying Weakness and Resistance).",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            effect=standard_attack,
        ),
        Attack(
            title='Mach Claw',
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=40,
            effect=standard_attack,
        ),
    ],
)

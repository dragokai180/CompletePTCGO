from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='75033e4f-93b7-5b1a-b342-611074eb6112',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bisharp.Name',
    display_name='Bisharp',
    searchable_by=['Bisharp', 'Stage 1', 'Bisharp'],
    subtypes=['Stage 1'],
    collector_number=82,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pawniard.Name',
    family_id=624,
    abilities=[
        Attack(
            title='Metal Sound',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.METAL: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Metal Wallop',
            game_text="During your next turn, this Pokémon's Metal Wallop attack does 40 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=standard_attack,
        ),
    ],
)

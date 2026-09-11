from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a934da46-f5cb-56e1-8626-cd0f919ec19b',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Swoobat.Name',
    display_name='Swoobat',
    searchable_by=['Swoobat', 'Stage 1', 'Swoobat'],
    subtypes=['Stage 1'],
    collector_number=72,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Woobat.Name',
    family_id=527,
    abilities=[
        Attack(
            title='Wave Amplification',
            game_text="During your next turn, this Pokémon's Returning Echo attack does 60 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Returning Echo',
            game_text='Flip a coin. If tails, return this Pokémon and all cards attached to it to your hand.',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=60,
            effect=standard_attack,
        ),
    ],
)

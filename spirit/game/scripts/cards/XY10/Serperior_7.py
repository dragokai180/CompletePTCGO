from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='90bf96b4-79f2-5099-8a53-d8d4660bb411',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Serperior.Name',
    display_name='Serperior',
    searchable_by=['Serperior', 'Stage 2', 'Serperior'],
    subtypes=['Stage 2'],
    collector_number=7,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Servine.Name',
    family_id=495,
    abilities=[
        Attack(
            title='Coil',
            game_text="During your next turn, this Pokémon's attacks do 60 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=standard_attack,
        ),
        Attack(
            title='Slashing Strike',
            game_text="This Pokémon can't use Slashing Strike during your next turn.",
            cost={PokemonTypes.GRASS: 1},
            damage=80,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)

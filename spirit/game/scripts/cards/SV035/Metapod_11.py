from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='45118137-2462-5818-bd1b-3540250730d1',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Metapod.Name',
    display_name='Metapod',
    searchable_by=['Metapod', 'Stage 1', 'Metapod'],
    subtypes=['Stage 1'],
    collector_number=11,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Caterpie.Name',
    family_id=10,
    abilities=[
        Attack(
            title='Tackle',
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
        Attack(
            title='Defensive Posture',
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage done to this Pokémon by attacks.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
    ],
)

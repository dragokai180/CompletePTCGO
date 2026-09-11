from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='02f93922-b63e-53dc-9cb5-d2af20c5853e',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Doublade.Name',
    display_name='Doublade',
    searchable_by=['Doublade', 'Stage 1', 'Doublade'],
    subtypes=['Stage 1'],
    collector_number=133,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Honedge.Name',
    family_id=679,
    abilities=[
        Attack(
            title='Swords Dance',
            game_text="During your next turn, this Pokémon's Slicing Blade attack does 80 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Slicing Blade',
            cost={PokemonTypes.METAL: 2},
            damage=40,
        ),
    ],
)

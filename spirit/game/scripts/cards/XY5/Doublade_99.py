from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='df30da94-95e3-5827-8011-fc88a7c64315',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Doublade.Name',
    display_name='Doublade',
    searchable_by=['Doublade', 'Stage 1', 'Doublade'],
    subtypes=['Stage 1'],
    collector_number=99,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Honedge.Name',
    family_id=679,
    abilities=[
        Attack(
            title='False Swipe',
            game_text="Flip a coin. If heads, put damage counters on your opponent's Active Pokémon until its remaining HP is 10.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Slash',
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)

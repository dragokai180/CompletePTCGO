from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='228d2b64-639f-5ad9-a9be-69a6886327a3',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Nuzleaf.Name',
    display_name='Nuzleaf',
    searchable_by=['Nuzleaf', 'Stage 1', 'Nuzleaf'],
    subtypes=['Stage 1'],
    collector_number=6,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Seedot.Name',
    family_id=273,
    abilities=[
        Attack(
            title='Razor Leaf',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title='Cut',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)

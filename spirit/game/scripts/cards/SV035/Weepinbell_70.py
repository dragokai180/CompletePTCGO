from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0be37850-dce0-55f7-bc9d-3c8f5edb2d3f',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Weepinbell.Name',
    display_name='Weepinbell',
    searchable_by=['Weepinbell', 'Stage 1', 'Weepinbell'],
    subtypes=['Stage 1'],
    collector_number=70,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Bellsprout.Name',
    family_id=69,
    abilities=[
        Attack(
            title='Cut',
            cost={PokemonTypes.GRASS: 1},
            damage=30,
        ),
        Attack(
            title='Spray Fluid',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)

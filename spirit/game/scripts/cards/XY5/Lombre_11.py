from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8c6d9990-f69c-583c-a4a7-a25004d04599',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lombre.Name',
    display_name='Lombre',
    searchable_by=['Lombre', 'Stage 1', 'Lombre'],
    subtypes=['Stage 1'],
    collector_number=11,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Lotad.Name',
    family_id=270,
    abilities=[
        Attack(
            title='Hook',
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
        Attack(
            title='Beat',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)

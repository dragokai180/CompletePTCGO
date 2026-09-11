from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='146b7b9a-717e-51db-a801-315745f8ec57',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name',
    display_name='Gloom',
    searchable_by=['Gloom', 'Stage 1', 'Gloom'],
    subtypes=['Stage 1'],
    collector_number=2,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Oddish.Name',
    family_id=43,
    abilities=[
        Attack(
            title='Drool',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)

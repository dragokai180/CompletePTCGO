from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8d5c69bd-c976-5467-9559-136edfa8553f',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kakuna.Name',
    display_name='Kakuna',
    searchable_by=['Kakuna', 'Stage 1', 'Kakuna'],
    subtypes=['Stage 1'],
    collector_number=2,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Weedle.Name',
    family_id=13,
    abilities=[
        Attack(
            title='Bug Bite',
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
    ],
)

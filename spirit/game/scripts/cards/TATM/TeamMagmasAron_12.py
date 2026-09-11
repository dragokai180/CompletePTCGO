from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c73e8546-e51d-5f25-b83a-fda5ffe48cb4',
    key='TATM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasAron.Name',
    display_name="Team Magma's Aron",
    searchable_by=["Team Magma's Aron", 'Basic', 'TeamMagmasAron'],
    subtypes=['Basic'],
    collector_number=12,
    set_code='TATM',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=304,
    abilities=[
        Attack(
            title='Gnaw',
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
    ],
)

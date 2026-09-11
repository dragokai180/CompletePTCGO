from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='72bfd9ed-7a82-5d3f-9c71-36520a71d942',
    key='HF',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Scyther.Name',
    display_name='Scyther',
    searchable_by=['Scyther', 'Basic', 'Scyther'],
    subtypes=['Basic'],
    collector_number=5,
    set_code='HF',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=123,
    abilities=[
        Attack(
            title='Slash',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
        Attack(
            title='Sharp Scythe',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)

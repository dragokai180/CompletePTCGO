from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fc19b09e-6904-5e70-8427-16b209956bc9',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sandile.Name',
    display_name='Sandile',
    searchable_by=['Sandile', 'Basic', 'Sandile'],
    subtypes=['Basic'],
    collector_number=115,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=551,
    abilities=[
        Attack(
            title='Gnaw',
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
        Attack(
            title='Ram',
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
        ),
    ],
)

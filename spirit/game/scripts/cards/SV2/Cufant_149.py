from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='40904b28-663f-51fd-b954-95d90f3c6071',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cufant.Name',
    display_name='Cufant',
    searchable_by=['Cufant', 'Basic', 'Cufant'],
    subtypes=['Basic'],
    collector_number=149,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=878,
    abilities=[
        Attack(
            title='Stampede',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)

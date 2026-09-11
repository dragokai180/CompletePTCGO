from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0cb35def-4ceb-598f-ae6e-0334ea0ad4cb',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lechonk.Name',
    display_name='Lechonk',
    searchable_by=['Lechonk', 'Basic', 'Lechonk'],
    subtypes=['Basic'],
    collector_number=182,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=915,
    abilities=[
        Attack(
            title='Headbutt Bounce',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Mud Shot',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)

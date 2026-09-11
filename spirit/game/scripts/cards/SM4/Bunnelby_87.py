from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='edcdf7ef-ce49-5df5-bad1-4b64aa205655',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bunnelby.Name',
    display_name='Bunnelby',
    searchable_by=['Bunnelby', 'Basic', 'Bunnelby'],
    subtypes=['Basic'],
    collector_number=87,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=659,
    abilities=[
        Attack(
            title='Mud Shot',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a80ed4e5-9ac9-53bb-b79a-b6509e23277c',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Capsakid.Name',
    display_name='Capsakid',
    searchable_by=['Capsakid', 'Basic', 'Capsakid'],
    subtypes=['Basic'],
    collector_number=24,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=951,
    abilities=[
        Attack(
            title='Double Headbutt',
            game_text='Flip 2 coins. This attack does 50 damage for each heads.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='725ecca4-f8f1-506a-ba07-69cc89d9d55f',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Capsakid.Name',
    display_name='Capsakid',
    searchable_by=['Capsakid', 'Basic', 'Capsakid'],
    subtypes=['Basic'],
    collector_number=23,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=951,
    abilities=[
        Attack(
            title='Reckless Charge',
            game_text='This Pokémon also does 10 damage to itself.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)

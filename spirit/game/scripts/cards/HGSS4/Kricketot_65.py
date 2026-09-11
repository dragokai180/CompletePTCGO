from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7a57cc93-935a-57ac-9d7f-3205fc11716c',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kricketot.Name',
    display_name='Kricketot',
    searchable_by=['Kricketot', 'Basic', 'Kricketot'],
    subtypes=['Basic'],
    collector_number=65,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=401,
    abilities=[
        Attack(
            title='Beat',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)

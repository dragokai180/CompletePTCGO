from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7bd9caa0-fd60-5fdd-a62e-b3e75b511b6f',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kricketot.Name',
    display_name='Kricketot',
    searchable_by=['Kricketot', 'Basic', 'Kricketot'],
    subtypes=['Basic'],
    collector_number=13,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=401,
    abilities=[
        Attack(
            title='Collect',
            game_text='Draw a card.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Bug Bite',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)

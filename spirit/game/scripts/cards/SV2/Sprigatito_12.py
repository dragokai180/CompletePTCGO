from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ab7c0ca2-1cbe-55ba-bc9e-4c21a5570002',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sprigatito.Name',
    display_name='Sprigatito',
    searchable_by=['Sprigatito', 'Basic', 'Sprigatito'],
    subtypes=['Basic'],
    collector_number=12,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=906,
    abilities=[
        Attack(
            title='Gather Sunlight',
            game_text='Search your deck for up to 2 Basic Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Seed Bomb',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='15e13f82-0df2-52c9-b08c-316f94f84079',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Smoliv.Name',
    display_name='Smoliv',
    searchable_by=['Smoliv', 'Basic', 'Smoliv'],
    subtypes=['Basic'],
    collector_number=21,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=928,
    abilities=[
        Attack(
            title='Nutrients',
            game_text='Heal 30 damage from 1 of your Pokémon.',
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Spray Fluid',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)

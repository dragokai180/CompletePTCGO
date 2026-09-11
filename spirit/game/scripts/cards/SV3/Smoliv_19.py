from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e17b4163-bd18-570d-92ea-48c5c265df89',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Smoliv.Name',
    display_name='Smoliv',
    searchable_by=['Smoliv', 'Basic', 'Smoliv'],
    subtypes=['Basic'],
    collector_number=19,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=928,
    abilities=[
        Attack(
            title='Absorb',
            game_text='Heal 10 damage from this Pokémon.',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)

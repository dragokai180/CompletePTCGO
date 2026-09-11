from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b1881018-07f8-5f55-84b6-ec23689d635e',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bramblin.Name',
    display_name='Bramblin',
    searchable_by=['Bramblin', 'Basic', 'Bramblin'],
    subtypes=['Basic'],
    collector_number=23,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=946,
    abilities=[
        Attack(
            title='Blot',
            game_text='Heal 10 damage from this Pokémon.',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='dda92478-6872-56be-96a4-bdbcba9e8c43',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bounsweet.Name',
    display_name='Bounsweet',
    searchable_by=['Bounsweet', 'Basic', 'Bounsweet'],
    subtypes=['Basic'],
    collector_number=8,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=761,
    abilities=[
        Attack(
            title='Quick Blow',
            game_text='Flip a coin. If heads, this attack does 20 more damage.',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

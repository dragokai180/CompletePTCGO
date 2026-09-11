from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='dd7a0079-6b98-5b51-bae2-cb9582a5e513',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Oddish.Name',
    display_name='Oddish',
    searchable_by=['Oddish', 'Basic', 'Oddish'],
    subtypes=['Basic'],
    collector_number=6,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=43,
    abilities=[
        Attack(
            title='Hook',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)

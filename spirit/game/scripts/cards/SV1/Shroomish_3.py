from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2d97ca00-a445-5705-92ac-dc3c390fd82d',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Shroomish.Name',
    display_name='Shroomish',
    searchable_by=['Shroomish', 'Basic', 'Shroomish'],
    subtypes=['Basic'],
    collector_number=3,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=285,
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

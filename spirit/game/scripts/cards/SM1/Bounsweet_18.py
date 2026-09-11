from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='394eeb26-0721-5251-89c9-1efd4a368685',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bounsweet.Name',
    display_name='Bounsweet',
    searchable_by=['Bounsweet', 'Basic', 'Bounsweet'],
    subtypes=['Basic'],
    collector_number=18,
    set_code='SM1',
    regulation_mark=None,
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
            title='Sweet Scent',
            game_text='Heal 30 damage from 1 of your Pokémon.',
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Splash',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)

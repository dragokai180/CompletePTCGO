from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3c50387b-eeaa-5d58-8f2f-158eedd2d259',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Karrablast.Name',
    display_name='Karrablast',
    searchable_by=['Karrablast', 'Basic', 'Karrablast'],
    subtypes=['Basic'],
    collector_number=12,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=588,
    abilities=[
        Attack(
            title='Take Down',
            game_text='This Pokémon does 10 damage to itself.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)

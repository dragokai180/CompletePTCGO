from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3a6fe586-2a2c-5788-8a49-e487551e6c7e',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Petilil.Name',
    display_name='Petilil',
    searchable_by=['Petilil', 'Basic', 'Petilil'],
    subtypes=['Basic'],
    collector_number=7,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=548,
    abilities=[
        Attack(
            title='Aromatherapy',
            game_text='Heal 10 damage from each of your Pokémon.',
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
    ],
)

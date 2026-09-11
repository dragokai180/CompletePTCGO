from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4af3d74b-fa5b-56b7-89e0-cad270e0848f',
    key='GUM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name',
    display_name='Magikarp',
    searchable_by=['Magikarp', 'Basic', 'Magikarp'],
    subtypes=['Basic'],
    collector_number=8,
    set_code='GUM',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=129,
    abilities=[
        Attack(
            title='Hold Still',
            game_text='Heal 10 damage from this Pokémon.',
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fcbf80ed-ae42-51a9-92a8-237b02f179ab',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Skorupi.Name',
    display_name='Skorupi',
    searchable_by=['Skorupi', 'Basic', 'Skorupi'],
    subtypes=['Basic'],
    collector_number=82,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=451,
    abilities=[
        Attack(
            title='Knock Off',
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Bug Bite',
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
        ),
    ],
)

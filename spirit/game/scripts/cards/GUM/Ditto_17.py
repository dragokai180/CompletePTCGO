from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ae95efb5-ae66-5519-a8b0-98d0584dcaf1',
    key='GUM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ditto.Name',
    display_name='Ditto',
    searchable_by=['Ditto', 'Basic', 'Ditto'],
    subtypes=['Basic'],
    collector_number=17,
    set_code='GUM',
    regulation_mark=None,
    rarity=Rarities.RareUltra,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=132,
    abilities=[
        Attack(
            title='Copy Anything',
            game_text="Choose 1 of your opponent's Pokémon's attacks and use it as this attack. If this Pokémon doesn't have the necessary Energy to use that attack, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)

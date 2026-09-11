from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='be961923-ffe1-5b74-8532-edeff093f636',
    key='GUM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name',
    display_name='Charmander',
    searchable_by=['Charmander', 'Basic', 'Charmander'],
    subtypes=['Basic'],
    collector_number=4,
    set_code='GUM',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=4,
    abilities=[
        Attack(
            title='Reckless Charge',
            game_text='This Pokémon does 10 damage to itself.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)

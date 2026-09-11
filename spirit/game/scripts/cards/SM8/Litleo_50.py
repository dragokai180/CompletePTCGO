from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0c89bbc8-caca-52fa-b5e5-e877913d56a4',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Litleo.Name',
    display_name='Litleo',
    searchable_by=['Litleo', 'Basic', 'Litleo'],
    subtypes=['Basic'],
    collector_number=50,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=667,
    abilities=[
        Ability(
            title='Wild Dash',
            game_text='If your opponent has any Pokémon-GX or Pokémon-EX in play, this Pokémon has no Retreat Cost.',
            passive=standard_passive('If your opponent has any Pokémon-GX or Pokémon-EX in play, this Pokémon has no Retreat Cost.'),
        ),
        Attack(
            title='Take Down',
            game_text='This Pokémon does 10 damage to itself.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)

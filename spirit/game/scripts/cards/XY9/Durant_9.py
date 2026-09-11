from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e92e0e0b-a002-569d-a8bb-24d64c1874cf',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Durant.Name',
    display_name='Durant',
    searchable_by=['Durant', 'Basic', 'Durant'],
    subtypes=['Basic'],
    collector_number=9,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=632,
    abilities=[
        Attack(
            title='Mountain Munch',
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=standard_attack,
        ),
        Attack(
            title='Scrape Down',
            game_text="If this Pokémon has any damage counters on it, discard the top 4 cards of your opponent's deck.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)

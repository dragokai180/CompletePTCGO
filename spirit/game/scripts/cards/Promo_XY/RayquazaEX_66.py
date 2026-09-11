from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3ab789bd-6dcc-5c21-a5d7-c7d85ddbb4cb',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.RayquazaEX.Name',
    display_name='Rayquaza-EX',
    searchable_by=['Rayquaza-EX', 'Basic', 'EX', 'RayquazaEX'],
    subtypes=['Basic', 'EX'],
    collector_number=66,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=384,
    abilities=[
        Attack(
            title='Mega Ascension',
            game_text='Search your deck for M Rayquaza-EX, reveal it, and put it into your hand. Shuffle your deck afterward.',
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Aeroscream',
            game_text='Flip a coin. If tails, discard 2 Energy attached to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 4},
            damage=130,
            effect=standard_attack,
        ),
    ],
)

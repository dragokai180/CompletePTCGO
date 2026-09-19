from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e8d7e70d-66b7-5bf8-9287-b610a071b3df',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sobble.Name',
    display_name='Sobble',
    searchable_by=['Sobble', 'Basic', 'Sobble'],
    subtypes=['Basic'],
    collector_number=73,
    set_code='Promo_SWSH',
    regulation_mark='D',
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'SWSH073'}},
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=816,
    abilities=[
        Attack(
            title='Growl',
            game_text="During your opponent's next turn, the Defending Pokémon's attacks do 20 less damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Rain Splash',
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)

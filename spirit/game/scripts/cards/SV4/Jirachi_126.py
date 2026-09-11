from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5bc26ff9-d3cf-5b42-85f8-53bfc109608f',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Jirachi.Name',
    display_name='Jirachi',
    searchable_by=['Jirachi', 'Basic', 'Jirachi'],
    subtypes=['Basic'],
    collector_number=126,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=385,
    abilities=[
        Ability(
            title='Stellar Veil',
            game_text="Prevent all damage counters from being placed on your Benched Pokémon by effects of attacks used by your opponent's Basic Pokémon.",
            passive=standard_passive("Prevent all damage counters from being placed on your Benched Pokémon by effects of attacks used by your opponent's Basic Pokémon."),
        ),
        Attack(
            title='Charge Energy',
            game_text='Search your deck for up to 2 Basic Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='342e73e3-3d53-5781-adc1-767e2f2b454b',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dondozo.Name',
    display_name='Dondozo',
    searchable_by=['Dondozo', 'Basic', 'Dondozo'],
    subtypes=['Basic'],
    collector_number=55,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=977,
    abilities=[
        Attack(
            title='Supplemental Swallow-Up',
            game_text='Look at the top 5 cards of your deck. You may attach any number of Basic Energy cards you find there to this Pokémon. Shuffle the other cards back into your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Hydro Splash',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 4},
            damage=180,
        ),
    ],
)

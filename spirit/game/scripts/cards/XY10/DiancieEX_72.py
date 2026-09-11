from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f5909e1a-2e35-59f0-b1d4-bdb4fcbcef7c',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.DiancieEX.Name',
    display_name='Diancie-EX',
    searchable_by=['Diancie-EX', 'Basic', 'EX', 'DiancieEX'],
    subtypes=['Basic', 'EX'],
    collector_number=72,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=150,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=719,
    abilities=[
        Ability(
            title='Sparkle Veil',
            game_text="As long as this Pokémon is your Active Pokémon, any damage done to your Pokémon by an opponent's attack is reduced by 30 (after applying Weakness and Resistance).",
            passive=standard_passive("As long as this Pokémon is your Active Pokémon, any damage done to your Pokémon by an opponent's attack is reduced by 30 (after applying Weakness and Resistance)."),
        ),
        Attack(
            title='Wonder Stage',
            game_text='If there is any Stadium card in play, this attack does 50 more damage.',
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

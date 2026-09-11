from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bfba4892-136a-5e6d-a607-3c9e8e979472',
    key='TwentiethAnn',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.BlastoiseEX.Name',
    display_name='Blastoise-EX',
    searchable_by=['Blastoise-EX', 'Basic', 'EX', 'BlastoiseEX'],
    subtypes=['Basic', 'EX'],
    collector_number=17,
    set_code='TwentiethAnn',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=9,
    abilities=[
        Attack(
            title='Hyper Whirlpool',
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
        Attack(
            title='Hydro Press',
            game_text="This attack does 20 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=standard_attack,
        ),
    ],
)

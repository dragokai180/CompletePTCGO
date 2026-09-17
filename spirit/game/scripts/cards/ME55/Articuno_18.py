from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1ff9db68-7fb8-5932-8596-cd58c3ca2c41',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Articuno.Name',
    display_name='Articuno',
    searchable_by=['Articuno', 'Basic', 'Articuno'],
    subtypes=['Basic'],
    collector_number=18,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=144,
    abilities=[
        Ability(
            title='Frosty Flapping',
            game_text='Once during your turn, if you have Moltres and Zapdos in play, you may use this Ability. Attach a Basic Water Energy card from your hand to this Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Hail',
            game_text="This attack does 30 damage to each of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)

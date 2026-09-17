from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c96c3ef0-daa4-5e27-84b2-cabd9eb9a9be',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Jirachiex.Name',
    display_name='Jirachi ex',
    searchable_by=['Jirachi ex', 'Basic', 'ex', 'Jirachiex'],
    subtypes=['Basic', 'ex'],
    collector_number=102,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.RareHoloEX,
    hp=160,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=20,
    family_id=385,
    abilities=[
        Attack(
            title='Wish Granter',
            game_text='Draw cards until you have 7 cards in your hand.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Swift',
            game_text="This attack's damage isn't affected by Weakness or Resistance, or by any effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)

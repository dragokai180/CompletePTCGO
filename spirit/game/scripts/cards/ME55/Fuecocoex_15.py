from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='90560cfc-1dab-5fe6-8cca-d6c6b76038df',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Fuecocoex.Name',
    display_name='Fuecoco ex',
    searchable_by=['Fuecoco ex', 'Basic', 'ex', 'Fuecocoex'],
    subtypes=['Basic', 'ex'],
    collector_number=15,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.RareHoloEX,
    hp=210,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=909,
    abilities=[
        Attack(
            title='Singe',
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Cheerful Flame',
            game_text='This attack does 70 damage for each Prize card you have taken.',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)

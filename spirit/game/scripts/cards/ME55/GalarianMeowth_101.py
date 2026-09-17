from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='161261a9-8c5d-55c2-aa6d-a00d764dbf08',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.GalarianMeowth.Name',
    display_name='Galarian Meowth',
    searchable_by=['Galarian Meowth', 'Basic', 'GalarianMeowth'],
    subtypes=['Basic'],
    collector_number=101,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=52,
    abilities=[
        Attack(
            title='Pay Day',
            game_text='Draw a card.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=standard_attack,
        ),
        Attack(
            title='Treasure Rush',
            game_text='This attack does 10 damage for each card in your hand.',
            cost={PokemonTypes.METAL: 1},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)

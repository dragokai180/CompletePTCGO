from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c7f5ffa8-ce80-5e20-829b-741d0144a237',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanMeowth.Name',
    display_name='Alolan Meowth',
    searchable_by=['Alolan Meowth', 'Basic', 'AlolanMeowth'],
    subtypes=['Basic'],
    collector_number=89,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=52,
    abilities=[
        Attack(
            title='Pay Day',
            game_text='Draw a card.',
            cost={},
            damage=10,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)

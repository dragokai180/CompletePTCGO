from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b680a900-20bf-5f83-97dc-935c96391c1d',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name',
    display_name='Vulpix',
    searchable_by=['Vulpix', 'Basic', 'Vulpix'],
    subtypes=['Basic'],
    collector_number=9,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=37,
    abilities=[
        Attack(
            title='Wild Kick',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)

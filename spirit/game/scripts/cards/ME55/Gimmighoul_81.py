from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f21e86dc-ea51-56d5-895a-985df6ef0109',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gimmighoul.Name',
    display_name='Gimmighoul',
    searchable_by=['Gimmighoul', 'Basic', 'Gimmighoul'],
    subtypes=['Basic'],
    collector_number=81,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=999,
    abilities=[
        Attack(
            title='Strolls So Much',
            game_text='Flip a coin. If heads, search your deck for a card and put it into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)

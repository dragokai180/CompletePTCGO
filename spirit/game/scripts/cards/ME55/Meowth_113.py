from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='00e291c1-9324-57cc-a55d-f6c8e0c397fa',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name',
    display_name='Meowth',
    searchable_by=['Meowth', 'Basic', 'Meowth'],
    subtypes=['Basic'],
    collector_number=113,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=52,
    abilities=[
        Attack(
            title='Pay Day',
            game_text='Draw a card.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)

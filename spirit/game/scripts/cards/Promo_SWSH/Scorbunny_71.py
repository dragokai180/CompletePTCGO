from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a5efb8b9-70bb-5724-89fc-9c95908a3586',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Scorbunny.Name',
    display_name='Scorbunny',
    searchable_by=['Scorbunny', 'Basic', 'Scorbunny'],
    subtypes=['Basic'],
    collector_number=71,
    set_code='Promo_SWSH',
    regulation_mark='D',
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'SWSH071'}},
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=813,
    abilities=[
        Attack(
            title='Me First',
            game_text='Draw a card.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Live Coal',
            cost={PokemonTypes.FIRE: 2},
            damage=20,
        ),
    ],
)

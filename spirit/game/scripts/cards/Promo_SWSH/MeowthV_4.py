from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='eaf73bb0-cf0d-5b49-b718-46c6732a2d8d',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MeowthV.Name',
    display_name='Meowth V',
    searchable_by=['Meowth V', 'Basic', 'V', 'MeowthV'],
    subtypes=['Basic', 'V'],
    collector_number=4,
    set_code='Promo_SWSH',
    regulation_mark='D',
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    attributes={200790: {'type': 'string', 'value': 'SWSH004'}},
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=52,
    abilities=[
        Attack(
            title='Pay Day',
            game_text='Draw a card.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Slashing Claw',
            cost={PokemonTypes.COLORLESS: 3},
            damage=130,
        ),
    ],
)

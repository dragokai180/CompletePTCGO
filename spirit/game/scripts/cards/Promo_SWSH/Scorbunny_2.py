from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cf5c7a57-2a4e-516f-a141-5c6ccfac52a3',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Scorbunny.Name',
    display_name='Scorbunny',
    searchable_by=['Scorbunny', 'Basic', 'Scorbunny'],
    subtypes=['Basic'],
    collector_number=2,
    set_code='Promo_SWSH',
    regulation_mark='D',
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'SWSH002'}},
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=813,
    abilities=[
        Attack(
            title='Super Singe',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)

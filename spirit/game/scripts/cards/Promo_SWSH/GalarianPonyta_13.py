from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1cf8528f-3f7a-56d7-9323-5c31ac6dacea',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.GalarianPonyta.Name',
    display_name='Galarian Ponyta',
    searchable_by=['Galarian Ponyta', 'Basic', 'GalarianPonyta'],
    subtypes=['Basic'],
    collector_number=13,
    set_code='Promo_SWSH',
    regulation_mark='D',
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'SWSH013'}},
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=77,
    abilities=[
        Attack(
            title='Heal Pulse',
            game_text='Heal 30 damage from 1 of your Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Flop',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)

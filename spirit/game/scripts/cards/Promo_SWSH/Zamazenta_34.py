from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d1bc213d-8829-5356-80d9-6e8e155968ee',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Zamazenta.Name',
    display_name='Zamazenta',
    searchable_by=['Zamazenta', 'Basic', 'Zamazenta'],
    subtypes=['Basic'],
    collector_number=34,
    set_code='Promo_SWSH',
    regulation_mark='D',
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    attributes={200790: {'type': 'string', 'value': 'SWSH034'}},
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=889,
    abilities=[
        Ability(
            title='Sturdy Shield',
            game_text='This Pokémon takes 20 less damage from attacks (after applying Weakness and Resistance).',
            passive=standard_passive('This Pokémon takes 20 less damage from attacks (after applying Weakness and Resistance).'),
        ),
        Attack(
            title='Headbang',
            cost={PokemonTypes.METAL: 3, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)

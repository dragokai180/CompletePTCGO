from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='34b81e79-7daf-58e2-960d-d78dd8e9e286',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Snorlax.Name',
    display_name='Snorlax',
    searchable_by=['Snorlax', 'Basic', 'Single Strike', 'Snorlax'],
    subtypes=['Basic', 'Single Strike'],
    collector_number=119,
    set_code='Promo_SWSH',
    regulation_mark='E',
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    attributes={200790: {'type': 'string', 'value': 'SWSH119'}},
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=143,
    abilities=[
        Attack(
            title='Slap Push',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title='Single Strike Tackle',
            game_text='This Pokémon also does 30 damage to itself.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=standard_attack,
        ),
    ],
)

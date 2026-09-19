from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9dbfc552-339f-5916-ab44-3f4b7b40e4a2',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name',
    display_name='Eevee',
    searchable_by=['Eevee', 'Basic', 'Eevee'],
    subtypes=['Basic'],
    collector_number=175,
    set_code='Promo_SWSH',
    regulation_mark='E',
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'SWSH175'}},
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=133,
    abilities=[
        Attack(
            title='Be Prepared',
            game_text='Attach a basic Energy card from your hand to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Bite',
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)

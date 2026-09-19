from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c82899ac-29dc-5737-a824-7f9e7fcf38b8',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.LancesCharizardV.Name',
    display_name="Lance's Charizard V",
    searchable_by=["Lance's Charizard V", 'Basic', 'V', 'LancesCharizardV'],
    subtypes=['Basic', 'V'],
    collector_number=133,
    set_code='Promo_SWSH',
    regulation_mark='E',
    rarity=Rarities.RarePromo,
    hp=220,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    attributes={200790: {'type': 'string', 'value': 'SWSH133'}},
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=6,
    abilities=[
        Attack(
            title='Flamethrower',
            game_text='Discard an Energy from this Pokémon.',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e6999596-3cef-53f0-bb83-5ae1a1f085b9',
    key='Promo_HGSS',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Porygon2.Name',
    display_name='Porygon2',
    searchable_by=['Porygon2', 'Stage 1', 'Porygon2'],
    subtypes=['Stage 1'],
    collector_number=23,
    set_code='Promo_HGSS',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    attributes={200790: {'type': 'string', 'value': 'HGSS23'}},
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Porygon.Name',
    family_id=137,
    abilities=[
        Ability(
            title='Shortcut',
            game_text='The Retreat Cost for each Porygon, Porygon2, and Porygon-Z you have in play is Colorless less.',
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive('The Retreat Cost for each Porygon, Porygon2, and Porygon-Z you have in play is Colorless less.'),
        ),
        Attack(
            title='Reckless Charge',
            game_text='Porygon2 does 10 damage to itself.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            effect=standard_attack,
        ),
    ],
)

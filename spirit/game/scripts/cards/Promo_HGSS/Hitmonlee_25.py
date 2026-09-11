from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d12cfed6-c0d6-54f1-bea7-66932681bc3a',
    key='Promo_HGSS',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hitmonlee.Name',
    display_name='Hitmonlee',
    searchable_by=['Hitmonlee', 'Basic', 'Hitmonlee'],
    subtypes=['Basic'],
    collector_number=25,
    set_code='Promo_HGSS',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    attributes={200790: {'type': 'string', 'value': 'HGSS25'}},
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=106,
    abilities=[
        Attack(
            title='Kick',
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
        ),
        Attack(
            title='High Jump Kick',
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)

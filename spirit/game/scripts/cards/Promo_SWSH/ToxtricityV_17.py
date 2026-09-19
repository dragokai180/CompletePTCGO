from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d53d2959-be39-5037-a77d-72cf34af0a03',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.ToxtricityV.Name',
    display_name='Toxtricity V',
    searchable_by=['Toxtricity V', 'Basic', 'V', 'ToxtricityV'],
    subtypes=['Basic', 'V'],
    collector_number=17,
    set_code='Promo_SWSH',
    regulation_mark='D',
    rarity=Rarities.RarePromo,
    hp=210,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    attributes={200790: {'type': 'string', 'value': 'SWSH017'}},
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=849,
    abilities=[
        Attack(
            title='Energize',
            game_text='Attach a Lightning Energy card from your discard pile to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Venom Slap',
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
        ),
    ],
)

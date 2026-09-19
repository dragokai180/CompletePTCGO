from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ab2ce3ea-e41f-5ff8-9887-87d0a0f9ac7a',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Jolteon.Name',
    display_name='Jolteon',
    searchable_by=['Jolteon', 'Stage 1', 'Jolteon'],
    subtypes=['Stage 1'],
    collector_number=94,
    set_code='Promo_SWSH',
    regulation_mark='D',
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    attributes={200790: {'type': 'string', 'value': 'SWSH094'}},
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name',
    family_id=133,
    abilities=[
        Attack(
            title='Energize',
            game_text='Attach a Lightning Energy card from your discard pile to this Pokémon.',
            cost={PokemonTypes.LIGHTNING: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Thunder',
            game_text='This Pokémon also does 30 damage to itself.',
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=standard_attack,
        ),
    ],
)

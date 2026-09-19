from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='da65f7e2-8a5c-54e1-ba79-d79cb8c3f18d',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Morpeko.Name',
    display_name='Morpeko',
    searchable_by=['Morpeko', 'Basic', 'Morpeko'],
    subtypes=['Basic'],
    collector_number=12,
    set_code='Promo_SWSH',
    regulation_mark='D',
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'SWSH012'}},
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=877,
    abilities=[
        Attack(
            title='Thunder Shock',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)

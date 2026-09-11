from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8e7e8914-39b9-5c0a-9f4e-54b52a4c6e4e',
    key='Promo_HGSS',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hitmonchan.Name',
    display_name='Hitmonchan',
    searchable_by=['Hitmonchan', 'Basic', 'Hitmonchan'],
    subtypes=['Basic'],
    collector_number=24,
    set_code='Promo_HGSS',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'HGSS24'}},
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=107,
    abilities=[
        Attack(
            title='Detect',
            game_text="Flip a coin. If heads, prevent all effects of attacks, including damage, done to Hitmonchan during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Sky Uppercut',
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a372bdb7-db5e-5f84-b1f2-d2d581a0d45e',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.ShadowRiderCalyrexV.Name',
    display_name='Shadow Rider Calyrex V',
    searchable_by=['Shadow Rider Calyrex V', 'Basic', 'V', 'ShadowRiderCalyrexV'],
    subtypes=['Basic', 'V'],
    collector_number=131,
    set_code='Promo_SWSH',
    regulation_mark='E',
    rarity=Rarities.RarePromo,
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    attributes={200790: {'type': 'string', 'value': 'SWSH131'}},
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=898,
    abilities=[
        Attack(
            title='Cloak in Shadows',
            game_text='Attach a Psychic Energy card from your discard pile to this Pokémon.',
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Hollow Binding',
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=standard_attack,
        ),
    ],
)

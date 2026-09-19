from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='171ec418-78be-5a53-9506-b8fcd5d850c6',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.HattereneV.Name',
    display_name='Hatterene V',
    searchable_by=['Hatterene V', 'Basic', 'V', 'HattereneV'],
    subtypes=['Basic', 'V'],
    collector_number=55,
    set_code='Promo_SWSH',
    regulation_mark='D',
    rarity=Rarities.RarePromo,
    hp=200,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    attributes={200790: {'type': 'string', 'value': 'SWSH055'}},
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=858,
    abilities=[
        Attack(
            title='Confounding Pulse',
            game_text="Switch 1 of your opponent's Benched Pokémon with their Active Pokémon. The new Active Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Mental Crush',
            game_text="If your opponent's Active Pokémon is Confused, this attack does 90 more damage.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

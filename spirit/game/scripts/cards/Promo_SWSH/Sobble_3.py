from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='878911cb-8f9d-5eab-9854-839423aeb783',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sobble.Name',
    display_name='Sobble',
    searchable_by=['Sobble', 'Basic', 'Sobble'],
    subtypes=['Basic'],
    collector_number=3,
    set_code='Promo_SWSH',
    regulation_mark='D',
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'SWSH003'}},
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=816,
    abilities=[
        Attack(
            title='Bind',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)

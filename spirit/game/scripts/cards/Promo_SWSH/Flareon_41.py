from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f744e9a7-c743-52fa-b01b-aa792d2103e7',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Flareon.Name',
    display_name='Flareon',
    searchable_by=['Flareon', 'Stage 1', 'Flareon'],
    subtypes=['Stage 1'],
    collector_number=41,
    set_code='Promo_SWSH',
    regulation_mark='D',
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    attributes={200790: {'type': 'string', 'value': 'SWSH041'}},
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name',
    family_id=133,
    abilities=[
        Attack(
            title='Singe',
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Kindle',
            game_text="Discard an Energy from this Pokémon. If you do, discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
        ),
    ],
)

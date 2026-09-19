from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6fefbe5a-0f7c-5544-a96f-918b07416ec3',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mimikyu.Name',
    display_name='Mimikyu δ',
    searchable_by=['Mimikyu δ', 'Basic', 'Mimikyu'],
    subtypes=['Basic'],
    collector_number=136,
    set_code='Promo_SWSH',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'SWSH136'}},
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=778,
    abilities=[
        Attack(
            title='Filch',
            game_text='Draw 2 cards.',
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Wet Claw',
            game_text="Put an Energy attached to your opponent's Active Pokémon into their hand.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2e776f79-c1b2-52f1-871c-8c970c6c7fa7',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Meltan.Name',
    display_name='Meltan',
    searchable_by=['Meltan', 'Basic', 'Meltan'],
    subtypes=['Basic'],
    collector_number=177,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=808,
    abilities=[
        Attack(
            title='Multiply',
            game_text='Search your deck for Meltan and put it onto your Bench. Then, shuffle your deck.',
            cost={PokemonTypes.METAL: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Beam',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)

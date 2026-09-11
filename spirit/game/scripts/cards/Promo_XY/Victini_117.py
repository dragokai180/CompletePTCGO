from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d4e8762f-6267-5d6f-855b-90628f8de941',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Victini.Name',
    display_name='Victini',
    searchable_by=['Victini', 'Basic', 'Victini'],
    subtypes=['Basic'],
    collector_number=117,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=494,
    abilities=[
        Attack(
            title='Energy Assist',
            game_text='Flip a coin. If heads, attach a basic Energy card from your discard pile to 1 of your Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Victory Ball',
            game_text='Discard a Fire Energy attached to this Pokémon.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=standard_attack,
        ),
    ],
)

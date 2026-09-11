from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bb5efee1-27c7-54c8-b394-2aaa4480d5d4',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Latios.Name',
    display_name='Latios',
    searchable_by=['Latios', 'Basic', 'Latios'],
    subtypes=['Basic'],
    collector_number=79,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=381,
    abilities=[
        Attack(
            title='Glide',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title='Sky Blade',
            game_text='If Latias is on your Bench, this attack does 50 more damage.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

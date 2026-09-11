from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='92904e58-b88e-50c3-91c2-e94c8565a10c',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bruxish.Name',
    display_name='Bruxish',
    searchable_by=['Bruxish', 'Basic', 'Bruxish'],
    subtypes=['Basic'],
    collector_number=11,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=779,
    abilities=[
        Attack(
            title='Vivid Charge',
            game_text='Search your deck for up to 3 basic Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Psychic Fang',
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=standard_attack,
        ),
    ],
)

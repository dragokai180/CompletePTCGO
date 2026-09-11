from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ec70e276-d3b9-5a6a-bc27-3f53b895855b',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Manaphy.Name',
    display_name='Manaphy',
    searchable_by=['Manaphy', 'Basic', 'Manaphy'],
    subtypes=['Basic'],
    collector_number=113,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=490,
    abilities=[
        Attack(
            title='Marine Guidance',
            game_text='Search your deck for a Water Pokémon, reveal it, and put it into your hand. Shuffle your deck afterward.',
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Aqua Ring',
            game_text='Switch this Pokémon with 1 of your Benched Pokémon.',
            cost={PokemonTypes.WATER: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f0f3cabd-d9bc-586c-8ad9-bdff999b3f0a',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Articuno.Name',
    display_name='Articuno',
    searchable_by=['Articuno', 'Basic', 'Articuno'],
    subtypes=['Basic'],
    collector_number=16,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=144,
    abilities=[
        Attack(
            title='Find Ice',
            game_text='Search your deck for up to 3 Water Energy cards, reveal them, and put them into your hand. Shuffle your deck afterward.',
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Freezing Wind',
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)

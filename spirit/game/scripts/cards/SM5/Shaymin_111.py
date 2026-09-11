from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='42ee43eb-f53a-5e8c-9e6a-dfaa3839c00e',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Shaymin.Name',
    display_name='Shaymin',
    searchable_by=['Shaymin', 'Basic', 'Shaymin'],
    subtypes=['Basic'],
    collector_number=111,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=492,
    abilities=[
        Attack(
            title='Call for Family',
            game_text='Search your deck for up to 2 Basic Pokémon and put them onto your Bench. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Glide',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)

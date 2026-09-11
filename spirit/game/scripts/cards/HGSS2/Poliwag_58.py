from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2aa2c34d-871a-550f-b3c7-b8a3d25f1eae',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Poliwag.Name',
    display_name='Poliwag',
    searchable_by=['Poliwag', 'Basic', 'Poliwag'],
    subtypes=['Basic'],
    collector_number=58,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=60,
    abilities=[
        Attack(
            title='Call for Family',
            game_text='Search your deck for a Basic Pokémon and put it onto your Bench. Shuffle your deck afterward.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Razor Fin',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)

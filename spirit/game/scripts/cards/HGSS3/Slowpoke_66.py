from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='269189a8-04ce-5724-a603-bb1b1d64707a',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name',
    display_name='Slowpoke',
    searchable_by=['Slowpoke', 'Basic', 'Slowpoke'],
    subtypes=['Basic'],
    collector_number=66,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=79,
    abilities=[
        Attack(
            title='Rambunctious Party',
            game_text='Look at the top 5 cards of your deck. Choose as many Basic Pokémon as you like and put them onto your Bench. Shuffle the other cards back into your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Rain Splash',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='081d8f1b-4cdd-54a2-b35d-7ff081bb324f',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Fomantis.Name',
    display_name='Fomantis',
    searchable_by=['Fomantis', 'Basic', 'Fomantis'],
    subtypes=['Basic'],
    collector_number=14,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=753,
    abilities=[
        Attack(
            title='Synthesis',
            game_text='Search your deck for a Grass Energy card and attach it to 1 of your Pokémon. Then, shuffle your deck.',
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Leafage',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)

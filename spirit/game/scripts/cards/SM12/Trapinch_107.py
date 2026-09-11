from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='89d00e69-d879-575c-a0fa-a25bb2fe797b',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Trapinch.Name',
    display_name='Trapinch',
    searchable_by=['Trapinch', 'Basic', 'Trapinch'],
    subtypes=['Basic'],
    collector_number=107,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=328,
    abilities=[
        Attack(
            title='Nest Building',
            game_text='Search your deck for a Stadium card, reveal it, and put it into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Sand Spray',
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
    ],
)

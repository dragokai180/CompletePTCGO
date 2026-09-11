from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b1e9f892-b9b3-52c7-a260-acd24d796eba',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Axew.Name',
    display_name='Axew',
    searchable_by=['Axew', 'Basic', 'Axew'],
    subtypes=['Basic'],
    collector_number=109,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=610,
    abilities=[
        Attack(
            title='Extra Chop',
            game_text='This Pokémon does 10 damage to itself.',
            cost={PokemonTypes.METAL: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Dragon Claw',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)

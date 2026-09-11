from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='990236bb-36d4-5492-928b-14a2b175c73c',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Deino.Name',
    display_name='Deino',
    searchable_by=['Deino', 'Basic', 'Deino'],
    subtypes=['Basic'],
    collector_number=84,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=633,
    abilities=[
        Attack(
            title='Roar',
            game_text='Your opponent switches his or her Active Pokémon with 1 of his or her Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Headbutt Bounce',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1},
            damage=20,
        ),
    ],
)

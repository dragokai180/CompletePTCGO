from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='508b7adf-030b-559e-8c46-d981d8e2cbd0',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Relicanth.Name',
    display_name='Relicanth',
    searchable_by=['Relicanth', 'Basic', 'Relicanth'],
    subtypes=['Basic'],
    collector_number=23,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=369,
    abilities=[
        Attack(
            title='Deep Sea Search',
            game_text='Search your deck for up to 2 Pokémon Tool cards, reveal them, and put them into your hand. Shuffle your deck afterward.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Take Down',
            game_text='This Pokémon does 10 damage to itself.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)

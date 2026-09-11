from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='997e7741-ae6e-57ac-a1cc-bd0902057f6d',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Yungoos.Name',
    display_name='Yungoos',
    searchable_by=['Yungoos', 'Basic', 'Yungoos'],
    subtypes=['Basic'],
    collector_number=112,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=734,
    abilities=[
        Attack(
            title='Scout',
            game_text='Your opponent reveals their hand.',
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

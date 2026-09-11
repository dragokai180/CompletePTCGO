from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4d2b7f8b-d399-5fc0-9978-a07bda6aa6ad',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pinsir.Name',
    display_name='Pinsir',
    searchable_by=['Pinsir', 'Basic', 'Pinsir'],
    subtypes=['Basic'],
    collector_number=4,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=127,
    abilities=[
        Attack(
            title='Grip and Squeeze',
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Hammer In',
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
        ),
    ],
)

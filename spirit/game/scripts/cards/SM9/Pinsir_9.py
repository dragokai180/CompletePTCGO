from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='76e06626-2eb6-56dd-980d-2ad0ad400e26',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pinsir.Name',
    display_name='Pinsir',
    searchable_by=['Pinsir', 'Basic', 'Pinsir'],
    subtypes=['Basic'],
    collector_number=9,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=127,
    abilities=[
        Attack(
            title='Grip and Squeeze',
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Guillotine Hug',
            game_text="Flip 2 coins. If both of them are heads, your opponent's Active Pokémon is Knocked Out.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
    ],
)

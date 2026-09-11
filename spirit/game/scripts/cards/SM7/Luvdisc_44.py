from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='86985b03-157f-553f-9d29-7c284be7df6d',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Luvdisc.Name',
    display_name='Luvdisc',
    searchable_by=['Luvdisc', 'Basic', 'Luvdisc'],
    subtypes=['Basic'],
    collector_number=44,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=370,
    abilities=[
        Attack(
            title='Even Game',
            game_text="Search your deck for a number of Basic Pokémon up to the number of your opponent's Benched Pokémon and put those Pokémon onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Water Pulse',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=standard_attack,
        ),
    ],
)

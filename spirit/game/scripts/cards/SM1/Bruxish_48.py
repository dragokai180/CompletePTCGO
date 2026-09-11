from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='214c2718-3532-54d7-a433-7b6d099e9aff',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bruxish.Name',
    display_name='Bruxish',
    searchable_by=['Bruxish', 'Basic', 'Bruxish'],
    subtypes=['Basic'],
    collector_number=48,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=779,
    abilities=[
        Attack(
            title='Vivid Charge',
            game_text='Search your deck for up to 3 basic Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Psychic Fangs',
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=standard_attack,
        ),
    ],
)

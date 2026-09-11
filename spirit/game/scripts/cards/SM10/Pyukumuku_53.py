from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a47c2a69-d7cc-5a1e-988b-bca65b3f3d89',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pyukumuku.Name',
    display_name='Pyukumuku',
    searchable_by=['Pyukumuku', 'Basic', 'Pyukumuku'],
    subtypes=['Basic'],
    collector_number=53,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=771,
    abilities=[
        Attack(
            title='Call for Family',
            game_text='Search your deck for up to 2 Basic Pokémon and put them onto your Bench. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Surprise Fist',
            game_text='You and your opponent play Rock-Paper-Scissors. If you win, this attack does 60 more damage.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

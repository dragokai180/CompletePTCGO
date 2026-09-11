from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ca9c6e56-7353-5a60-a98d-7e832eec54ee',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGeodude.Name',
    display_name='Alolan Geodude',
    searchable_by=['Alolan Geodude', 'Basic', 'AlolanGeodude'],
    subtypes=['Basic'],
    collector_number=35,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=74,
    abilities=[
        Attack(
            title='Charge',
            game_text='Search your deck for up to 2 Lightning Energy cards and attach them to this Pokémon. Then, shuffle your deck.',
            cost={},
            effect=standard_attack,
        ),
        Attack(
            title='Smash Bomb',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=standard_attack,
        ),
    ],
)

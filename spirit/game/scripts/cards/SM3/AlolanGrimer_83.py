from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='01a67a91-6027-5b87-82a5-66736e3fb6b1',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGrimer.Name',
    display_name='Alolan Grimer',
    searchable_by=['Alolan Grimer', 'Basic', 'AlolanGrimer'],
    subtypes=['Basic'],
    collector_number=83,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=88,
    abilities=[
        Attack(
            title='Division',
            game_text='Search your deck for Alolan Grimer and put it onto your Bench. Then, shuffle your deck.',
            cost={},
            effect=standard_attack,
        ),
        Attack(
            title='Slippery Sludge',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
    ],
)

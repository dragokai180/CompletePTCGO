from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='42bbf677-7a8e-53ec-884c-f8a5a2237f07',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Oranguru.Name',
    display_name='Oranguru',
    searchable_by=['Oranguru', 'Basic', 'Oranguru'],
    subtypes=['Basic'],
    collector_number=182,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=765,
    abilities=[
        Attack(
            title="Sage's Riddle",
            game_text='Put a Pokémon from your hand face down in front of you. Your opponent guesses the type of that Pokémon, and then you reveal it. If your opponent guessed right, they draw 4 cards. If they guessed wrong, you draw 4 cards. Return the Pokémon to your hand.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Gentle Slap',
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)

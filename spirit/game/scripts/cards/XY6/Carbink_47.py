from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='691c1480-4aa7-5c6f-9b25-24d84f79df91',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Carbink.Name',
    display_name='Carbink',
    searchable_by=['Carbink', 'Basic', 'Carbink'],
    subtypes=['Basic'],
    collector_number=47,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=703,
    abilities=[
        Ability(
            title='Jewel Armor',
            game_text="As long as this Pokémon is on your Bench, prevent all damage done to this Pokémon by attacks (both yours and your opponent's).",
            passive=standard_passive("As long as this Pokémon is on your Bench, prevent all damage done to this Pokémon by attacks (both yours and your opponent's)."),
        ),
        Attack(
            title='Spin Tackle',
            game_text='Flip a coin. If tails, this Pokémon does 20 damage to itself.',
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)

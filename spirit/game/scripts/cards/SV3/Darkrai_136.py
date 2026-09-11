from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='96c93cf5-15cc-5ef1-acca-37fc7cf03ca6',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Darkrai.Name',
    display_name='Darkrai',
    searchable_by=['Darkrai', 'Basic', 'Darkrai'],
    subtypes=['Basic'],
    collector_number=136,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=491,
    abilities=[
        Attack(
            title='Dark Slumber',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Night Cyclone',
            game_text='Move all Energy from this Pokémon to your Benched Pokémon in any way you like.',
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
        ),
    ],
)

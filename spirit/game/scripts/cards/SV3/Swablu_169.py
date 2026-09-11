from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fe0292d9-4a46-5316-a4d6-44903c0c4b42',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Swablu.Name',
    display_name='Swablu',
    searchable_by=['Swablu', 'Basic', 'Swablu'],
    subtypes=['Basic'],
    collector_number=169,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=333,
    abilities=[
        Attack(
            title='Fluffy Guard',
            game_text="During your opponent's next turn, this Pokémon takes 20 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Flap',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)

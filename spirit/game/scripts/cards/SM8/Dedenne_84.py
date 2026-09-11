from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b20292b0-f110-5644-a123-1fbfe797dd9d',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dedenne.Name',
    display_name='Dedenne',
    searchable_by=['Dedenne', 'Basic', 'Dedenne'],
    subtypes=['Basic'],
    collector_number=84,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=702,
    abilities=[
        Attack(
            title='Nuzzle',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Nuzzle Shot',
            game_text="This attack does 10 damage for each of your Pokémon in play that has the Nuzzle attack to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=standard_attack,
        ),
    ],
)

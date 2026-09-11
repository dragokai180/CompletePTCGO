from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='dc177a17-d948-5b9d-a70f-4ec9cb0c5879',
    key='DM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Trapinch.Name',
    display_name='Trapinch',
    searchable_by=['Trapinch', 'Basic', 'Trapinch'],
    subtypes=['Basic'],
    collector_number=32,
    set_code='DM',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=328,
    abilities=[
        Attack(
            title='Mini Earthquake',
            game_text="This attack does 10 damage to each of your Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)

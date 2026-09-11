from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='78b3a614-a751-5fb1-b8b8-ad3c0f8d7bce',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Meloetta.Name',
    display_name='Meloetta',
    searchable_by=['Meloetta', 'Basic', 'Meloetta'],
    subtypes=['Basic'],
    collector_number=104,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=648,
    abilities=[
        Attack(
            title='Sing',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Miracle Harmony',
            game_text="Flip a coin for each of your Pokémon in play that has the Sing attack. This attack does 10 damage for each heads to each of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
    ],
)

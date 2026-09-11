from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='23b30fff-f5b9-5be0-94e0-00fc539c7c44',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Beedrill.Name',
    display_name='Beedrill',
    searchable_by=['Beedrill', 'Stage 2', 'Beedrill'],
    subtypes=['Stage 2'],
    collector_number=7,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Kakuna.Name',
    family_id=13,
    abilities=[
        Attack(
            title='Poison Sting',
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Swarming Sting',
            game_text="This attack does 40 damage times the number of Beedrill you have in play to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)

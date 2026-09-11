from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d19df7ee-5088-53a6-b19a-fe41f0398b65',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Swampert.Name',
    display_name='Swampert',
    searchable_by=['Swampert', 'Stage 2', 'Swampert'],
    subtypes=['Stage 2'],
    collector_number=35,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Marshtomp.Name',
    family_id=258,
    abilities=[
        Attack(
            title='Water Arrow',
            game_text="This attack does 60 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Waterfall',
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
    ],
)

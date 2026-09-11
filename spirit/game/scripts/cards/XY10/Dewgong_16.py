from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cd61f446-997e-52bc-beac-185d45eae92d',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dewgong.Name',
    display_name='Dewgong',
    searchable_by=['Dewgong', 'Stage 1', 'Dewgong'],
    subtypes=['Stage 1'],
    collector_number=16,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Seel.Name',
    family_id=86,
    abilities=[
        Attack(
            title='Freezing Breath',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed. If tails, your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Aurora Beam',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=100,
        ),
    ],
)

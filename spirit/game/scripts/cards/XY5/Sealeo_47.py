from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5d548648-18ea-57b9-b3f0-d60b82b0bf63',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sealeo.Name',
    display_name='Sealeo',
    searchable_by=['Sealeo', 'Stage 1', 'Sealeo'],
    subtypes=['Stage 1'],
    collector_number=47,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Spheal.Name',
    family_id=363,
    abilities=[
        Attack(
            title='Freezing Headbutt',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Aurora Beam',
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)

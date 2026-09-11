from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5d78a0af-6949-5c29-a7d7-8fb29c99ef42',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Spewpa.Name',
    display_name='Spewpa',
    searchable_by=['Spewpa', 'Stage 1', 'Spewpa'],
    subtypes=['Stage 1'],
    collector_number=16,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Scatterbug.Name',
    family_id=664,
    abilities=[
        Attack(
            title='Bug Bite',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Stun Spore',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=standard_attack,
        ),
    ],
)

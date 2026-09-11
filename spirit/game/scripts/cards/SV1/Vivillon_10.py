from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='745afa28-9a03-5265-bef3-af08d9730f63',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Vivillon.Name',
    display_name='Vivillon',
    searchable_by=['Vivillon', 'Stage 2', 'Vivillon'],
    subtypes=['Stage 2'],
    collector_number=10,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Spewpa.Name',
    family_id=664,
    abilities=[
        Attack(
            title='Miracle Powder',
            game_text="Flip a coin. If heads, choose a Special Condition. Your opponent's Active Pokémon is now affected by that Special Condition.",
            cost={PokemonTypes.GRASS: 1},
            damage=50,
            effect=standard_attack,
        ),
        Attack(
            title='Bug Buzz',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)

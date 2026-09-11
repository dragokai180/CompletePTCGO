from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8184ddae-4d9d-5991-a90f-3e4632a2e260',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Vanilluxe.Name',
    display_name='Vanilluxe',
    searchable_by=['Vanilluxe', 'Stage 2', 'Vanilluxe'],
    subtypes=['Stage 2'],
    collector_number=35,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Vanillish.Name',
    family_id=582,
    abilities=[
        Attack(
            title='Hail',
            game_text="This attack does 20 damage to each of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Frozen Breath',
            game_text="You may discard 2 Water Energy from this Pokémon. If you do, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.WATER: 3},
            damage=80,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e73607c0-2e45-5220-86f8-a0dc5a6c8a3c',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ferrothorn.Name',
    display_name='Ferrothorn',
    searchable_by=['Ferrothorn', 'Stage 1', 'Ferrothorn'],
    subtypes=['Stage 1'],
    collector_number=103,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Ferroseed.Name',
    family_id=597,
    abilities=[
        Attack(
            title='Guard Press',
            game_text="During your opponent's next turn, this Pokémon takes 20 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Thorn Pod Throw',
            game_text="This attack does 20 damage times the amount of Metal Energy attached to this Pokémon to 1 of your opponent's Benched Pokémon. You can't do more than 100 damage to a Benched Pokémon in this way. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=standard_attack,
        ),
    ],
)

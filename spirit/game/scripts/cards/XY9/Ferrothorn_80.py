from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='55f307fa-302e-50c1-b0ad-193c715f5f82',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ferrothorn.Name',
    display_name='Ferrothorn',
    searchable_by=['Ferrothorn', 'Stage 1', 'Ferrothorn'],
    subtypes=['Stage 1'],
    collector_number=80,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
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
            title='Metal Claw',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title='Spike Lash',
            game_text="This attack does 10 damage to each of your opponent's Pokémon for each Colorless in that Pokémon's Retreat Cost. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='49a25195-b8ad-5616-bfd5-e5a3d9c6c9a2',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Simisage.Name',
    display_name='Simisage',
    searchable_by=['Simisage', 'Stage 1', 'Simisage'],
    subtypes=['Stage 1'],
    collector_number=11,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pansage.Name',
    family_id=511,
    abilities=[
        Attack(
            title='Torment',
            game_text="Choose 1 of your opponent's Active Pokémon's attacks. That Pokémon can't use that attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
            locks_next_turn=True,
        ),
        Attack(
            title='Solar Beam',
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)

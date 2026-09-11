from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e7b2514a-ff88-5967-83b0-c14e81ae7be5',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dodrio.Name',
    display_name='Dodrio',
    searchable_by=['Dodrio', 'Stage 1', 'Dodrio'],
    subtypes=['Stage 1'],
    collector_number=151,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Doduo.Name',
    family_id=84,
    abilities=[
        Attack(
            title='Tri Attack',
            game_text='Flip 3 coins. This attack does 60 damage for each heads.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Accelerating Stab',
            game_text="This Pokémon can't use Accelerating Stab during your next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)

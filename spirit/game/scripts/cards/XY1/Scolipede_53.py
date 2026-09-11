from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='36f203c1-e092-5283-9e66-5ce41c260c2d',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Scolipede.Name',
    display_name='Scolipede',
    searchable_by=['Scolipede', 'Stage 2', 'Scolipede'],
    subtypes=['Stage 2'],
    collector_number=53,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Whirlipede.Name',
    family_id=543,
    abilities=[
        Attack(
            title='Random Peck',
            game_text='Flip 2 coins. This attack does 20 more damage for each heads.',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Poison Ring',
            game_text="Your opponent's Active Pokémon is now Poisoned. That Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 3},
            damage=70,
            effect=standard_attack,
        ),
    ],
)

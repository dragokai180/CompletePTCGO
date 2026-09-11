from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='aee6d470-2aa7-52b0-bcb3-7bea61321ffb',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Grumpig.Name',
    display_name='Grumpig',
    searchable_by=['Grumpig', 'Stage 1', 'Grumpig'],
    subtypes=['Stage 1'],
    collector_number=31,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Spoink.Name',
    family_id=325,
    abilities=[
        Attack(
            title='Head Walking',
            game_text="Put a Basic Pokémon from your opponent's discard pile onto his or her Bench. Then, put 3 damage counters on that Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Knock Back',
            game_text='Your opponent switches his or her Active Pokémon with 1 of his or her Benched Pokémon.',
            cost={PokemonTypes.PSYCHIC: 2},
            damage=50,
            effect=standard_attack,
        ),
    ],
)

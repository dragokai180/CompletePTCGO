from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3132052f-c8da-58d9-a9a7-5e3d8b7bb611',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Grumpig.Name',
    display_name='Grumpig',
    searchable_by=['Grumpig', 'Stage 1', 'Grumpig'],
    subtypes=['Stage 1'],
    collector_number=23,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Spoink.Name',
    family_id=325,
    abilities=[
        Attack(
            title='Psychic Lock',
            game_text="Your opponent can't use any Poké-Powers on his or her Pokémon during his or her next turn.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
            locks_next_turn=True,
        ),
        Attack(
            title='Bench Manipulation',
            game_text="Your opponent flips a coin for each of his or her Benched Pokémon. This attack does 40 damage times the number of tails. This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)

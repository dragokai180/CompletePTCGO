from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2afe32f0-e2d3-5b1d-8922-4d56925f0174',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Galvantula.Name',
    display_name='Galvantula',
    searchable_by=['Galvantula', 'Stage 1', 'Galvantula'],
    subtypes=['Stage 1'],
    collector_number=42,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.LIGHTNING, PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Joltik.Name',
    family_id=595,
    abilities=[
        Attack(
            title='Double Thread',
            game_text="This attack does 30 damage to 2 of your opponent's Pokémon. Also apply Weakness and Resistance for Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Electroweb',
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)

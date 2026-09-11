from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e3246684-0f7f-533b-aab4-75a933b07d17',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Galvantula.Name',
    display_name='Galvantula',
    searchable_by=['Galvantula', 'Stage 1', 'Galvantula'],
    subtypes=['Stage 1'],
    collector_number=27,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
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
            title='Cobweb Trip',
            game_text="Switch 1 of your opponent's Benched Pokémon with your opponent's Active Pokémon. The new Active Pokémon is now Confused.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Electroweb',
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)

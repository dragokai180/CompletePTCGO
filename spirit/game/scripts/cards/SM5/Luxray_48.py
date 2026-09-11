from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6164397e-2c24-53b7-8b59-0e53f63d5759',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Luxray.Name',
    display_name='Luxray',
    searchable_by=['Luxray', 'Stage 2', 'Luxray'],
    subtypes=['Stage 2'],
    collector_number=48,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Luxio.Name',
    family_id=403,
    abilities=[
        Ability(
            title='Intimidating Fang',
            game_text="As long as this Pokémon is your Active Pokémon, your opponent's Active Pokémon's attacks do 30 less damage (before applying Weakness and Resistance).",
            passive=standard_passive("As long as this Pokémon is your Active Pokémon, your opponent's Active Pokémon's attacks do 30 less damage (before applying Weakness and Resistance)."),
        ),
        Attack(
            title='Volt Bolt',
            game_text="Discard all Lightning Energy from this Pokémon. This attack does 150 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)

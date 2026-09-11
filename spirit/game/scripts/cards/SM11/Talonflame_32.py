from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='41110c2a-2cd0-50ce-a7ea-798b624a4182',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Talonflame.Name',
    display_name='Talonflame',
    searchable_by=['Talonflame', 'Stage 2', 'Talonflame'],
    subtypes=['Stage 2'],
    collector_number=32,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Fletchinder.Name',
    family_id=661,
    abilities=[
        Attack(
            title='Heat Wave',
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            damage=40,
            effect=standard_attack,
        ),
        Attack(
            title='Flare Raid',
            game_text="Discard an Energy from this Pokémon. This attack does 50 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=standard_attack,
        ),
    ],
)

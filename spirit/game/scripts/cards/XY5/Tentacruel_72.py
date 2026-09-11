from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='82903d23-01f5-58d6-95d4-9aedd59cb712',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tentacruel.Name',
    display_name='Tentacruel',
    searchable_by=['Tentacruel', 'Stage 1', 'Tentacruel'],
    subtypes=['Stage 1'],
    collector_number=72,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tentacool.Name',
    family_id=72,
    abilities=[
        Attack(
            title='Dancing Tentacles',
            game_text="Your opponent's Active Pokémon is now Confused and Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Stick and Absorb',
            game_text="Heal 30 damage from this Pokémon. The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='92e2d2b3-87f4-5632-ae97-6b347e51b2ea',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Liepard.Name',
    display_name='Liepard',
    searchable_by=['Liepard', 'Stage 1', 'Liepard'],
    subtypes=['Stage 1'],
    collector_number=136,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Purrloin.Name',
    family_id=509,
    abilities=[
        Attack(
            title='Scratch',
            cost={PokemonTypes.DARKNESS: 1},
            damage=40,
        ),
        Attack(
            title='Shadow Scratch',
            game_text="If the Defending Pokémon is a Basic Pokémon, it can't attack during your opponent's next turn.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=standard_attack,
        ),
    ],
)

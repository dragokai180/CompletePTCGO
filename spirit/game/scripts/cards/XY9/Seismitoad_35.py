from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ae58c071-f371-5d56-8258-bcfa757d06b9',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Seismitoad.Name',
    display_name='Seismitoad',
    searchable_by=['Seismitoad', 'Stage 2', 'Seismitoad'],
    subtypes=['Stage 2'],
    collector_number=35,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Palpitoad.Name',
    family_id=535,
    abilities=[
        Attack(
            title='Siphon Off',
            game_text='Attach 3 Energy cards from your discard pile to this Pokémon.',
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Shaky Fall',
            game_text="Your opponent's Active Pokémon is now Confused. That Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.WATER: 4},
            damage=90,
            effect=standard_attack,
        ),
    ],
)

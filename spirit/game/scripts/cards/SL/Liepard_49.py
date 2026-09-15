from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3f7a425b-2558-5e61-94f8-e86279b024b7',
    key='SL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Liepard.Name',
    display_name='Liepard',
    searchable_by=['Liepard', 'Stage 1', 'Liepard'],
    subtypes=['Stage 1'],
    collector_number=49,
    set_code='SL',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
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
            title='Torment',
            game_text="Choose 1 of your opponent's Active Pokémon's attacks. That Pokémon can't use that attack during your opponent's next turn.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            effect=standard_attack,
            locks_next_turn=False,
        ),
        Attack(
            title='Slash',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)

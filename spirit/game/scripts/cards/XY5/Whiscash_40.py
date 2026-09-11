from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='754bb4e4-824d-561f-8cac-4bcaf83e1bab',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Whiscash.Name',
    display_name='Whiscash',
    searchable_by=['Whiscash', 'Stage 1', 'Whiscash'],
    subtypes=['Stage 1'],
    collector_number=40,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Barboach.Name',
    family_id=339,
    abilities=[
        Attack(
            title='Amnesia',
            game_text="Choose 1 of your opponent's Active Pokémon's attacks. That Pokémon can't use that attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
            locks_next_turn=True,
        ),
        Attack(
            title='Rising Lunge',
            game_text='Flip a coin. If heads, this attack does 30 more damage.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

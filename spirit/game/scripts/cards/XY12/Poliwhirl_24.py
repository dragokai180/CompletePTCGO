from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c43ecdc1-497f-5963-a9d7-fead4deb878e',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Poliwhirl.Name',
    display_name='Poliwhirl',
    searchable_by=['Poliwhirl', 'Stage 1', 'Poliwhirl'],
    subtypes=['Stage 1'],
    collector_number=24,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Poliwag.Name',
    family_id=60,
    abilities=[
        Attack(
            title='Amnesia',
            game_text="Choose 1 of your opponent's Active Pokémon's attacks. That Pokémon can't use that attack during your opponent's next turn.",
            cost={PokemonTypes.WATER: 2},
            damage=30,
            effect=standard_attack,
            locks_next_turn=True,
        ),
        Attack(
            title='Double Slap',
            game_text='Flip 2 coins. This attack does 50 damage times the number of heads.',
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f774ff89-8c12-594a-9f15-324e2fc22010',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Fearow.Name',
    display_name='Fearow',
    searchable_by=['Fearow', 'Stage 1', 'Fearow'],
    subtypes=['Stage 1'],
    collector_number=66,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Spearow.Name',
    family_id=21,
    abilities=[
        Attack(
            title='Peck',
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title='Drill Run',
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=70,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='43c9ed64-fd7c-504f-87c6-8e5a6dc1e317',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tyrantrum.Name',
    display_name='Tyrantrum',
    searchable_by=['Tyrantrum', 'Stage 1', 'Tyrantrum'],
    subtypes=['Stage 1'],
    collector_number=62,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tyrunt.Name',
    family_id=696,
    abilities=[
        Attack(
            title='Chew Up',
            game_text="If your opponent's Active Pokémon has any Special Energy attached to it, this attack does 90 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Giga Impact',
            game_text="This Pokémon can't attack during your next turn.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=standard_attack,
        ),
    ],
)

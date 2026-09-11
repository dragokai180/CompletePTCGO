from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='32450d05-0c62-527f-8283-1ae43d4d3767',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kakuna.Name',
    display_name='Kakuna',
    searchable_by=['Kakuna', 'Stage 1', 'Kakuna'],
    subtypes=['Stage 1'],
    collector_number=6,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Weedle.Name',
    family_id=13,
    abilities=[
        Attack(
            title='Stiffen',
            game_text="During your opponent's next turn, any damage done to this Pokémon by attacks is reduced by 40 (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Poison Powder',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.GRASS: 2},
            damage=20,
            effect=standard_attack,
        ),
    ],
)

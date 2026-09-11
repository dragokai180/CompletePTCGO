from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='700e634c-3d24-5ec6-b7e3-713539d0bc5e',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Metapod.Name',
    display_name='Metapod',
    searchable_by=['Metapod', 'Stage 1', 'Metapod'],
    subtypes=['Stage 1'],
    collector_number=4,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Caterpie.Name',
    family_id=10,
    abilities=[
        Attack(
            title='Stiffen',
            game_text="During your opponent's next turn, any damage done to this Pokémon by attacks is reduced by 40 (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Stun Spore',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 2},
            damage=20,
            effect=standard_attack,
        ),
    ],
)

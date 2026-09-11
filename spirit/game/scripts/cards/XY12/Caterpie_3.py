from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7d9971d0-1aaa-52f8-93cc-8bcbd5caa81b',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Caterpie.Name',
    display_name='Caterpie',
    searchable_by=['Caterpie', 'Basic', 'Caterpie'],
    subtypes=['Basic'],
    collector_number=3,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=10,
    abilities=[
        Attack(
            title='String Shot',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)

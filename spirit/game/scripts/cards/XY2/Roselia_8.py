from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1cb5a448-1154-5a1c-aa20-21c4c9a5f773',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Roselia.Name',
    display_name='Roselia',
    searchable_by=['Roselia', 'Basic', 'Roselia'],
    subtypes=['Basic'],
    collector_number=8,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=315,
    abilities=[
        Attack(
            title='Sleep Powder',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=standard_attack,
        ),
        Attack(
            title='Cut',
            cost={PokemonTypes.GRASS: 2},
            damage=20,
        ),
    ],
)

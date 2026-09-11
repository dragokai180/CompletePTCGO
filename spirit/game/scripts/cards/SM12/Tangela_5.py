from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8ac702c1-fea6-5279-9e33-168f81800de5',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tangela.Name',
    display_name='Tangela',
    searchable_by=['Tangela', 'Basic', 'Tangela'],
    subtypes=['Basic'],
    collector_number=5,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=114,
    abilities=[
        Attack(
            title='Toxic',
            game_text="Your opponent's Active Pokémon is now Poisoned. Put 2 damage counters instead of 1 on that Pokémon between turns.",
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
    ],
)

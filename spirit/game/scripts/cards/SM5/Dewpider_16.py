from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='52d6443c-a1b4-5f2b-911f-89e4d99ff7a2',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dewpider.Name',
    display_name='Dewpider',
    searchable_by=['Dewpider', 'Basic', 'Dewpider'],
    subtypes=['Basic'],
    collector_number=16,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=751,
    abilities=[
        Attack(
            title='Bubble',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)

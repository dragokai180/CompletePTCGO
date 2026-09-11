from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e26c5e9d-1d85-5d45-88c9-a282639ffb11',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Spinarak.Name',
    display_name='Spinarak',
    searchable_by=['Spinarak', 'Basic', 'Spinarak'],
    subtypes=['Basic'],
    collector_number=5,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=167,
    abilities=[
        Attack(
            title='Stun Poison',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed and Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Pierce',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)

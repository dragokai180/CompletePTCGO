from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c0de1a89-da15-5c3f-9b4a-023d4b25da79',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Magby.Name',
    display_name='Magby',
    searchable_by=['Magby', 'Basic', 'Magby'],
    subtypes=['Basic'],
    collector_number=19,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=240,
    abilities=[
        Attack(
            title='Scorching Heater',
            game_text="During your opponent's next turn, if this Pokémon is damaged by an attack (even if it is Knocked Out), put 6 damage counters on the Attacking Pokémon.",
            cost={},
            effect=standard_attack,
        ),
    ],
)

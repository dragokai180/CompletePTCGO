from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e0193a99-0d26-513b-8328-498e4151e5a5',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Clamperl.Name',
    display_name='Clamperl',
    searchable_by=['Clamperl', 'Basic', 'Clamperl'],
    subtypes=['Basic'],
    collector_number=49,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=366,
    abilities=[
        Attack(
            title='Shell Protection',
            game_text="During your opponent's next turn, if this Pokémon would be damaged by an attack, prevent that attack's damage done to this Pokémon if that damage is 50 or less.",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
    ],
)

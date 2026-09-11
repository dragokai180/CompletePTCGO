from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3f0add16-1668-56c8-b576-59975d8a5f1c',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Skrelp.Name',
    display_name='Skrelp',
    searchable_by=['Skrelp', 'Basic', 'Skrelp'],
    subtypes=['Basic'],
    collector_number=44,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=690,
    abilities=[
        Attack(
            title='Spit Poison',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
    ],
)

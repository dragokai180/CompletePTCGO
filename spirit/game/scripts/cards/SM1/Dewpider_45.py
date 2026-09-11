from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e9348206-2a98-59f9-9576-3483d0ec9352',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dewpider.Name',
    display_name='Dewpider',
    searchable_by=['Dewpider', 'Basic', 'Dewpider'],
    subtypes=['Basic'],
    collector_number=45,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=751,
    abilities=[
        Attack(
            title='Bubble',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)

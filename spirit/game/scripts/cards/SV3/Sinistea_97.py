from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1dba69cb-1dcb-5ac6-a217-9a0911f47ff8',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sinistea.Name',
    display_name='Sinistea',
    searchable_by=['Sinistea', 'Basic', 'Sinistea'],
    subtypes=['Basic'],
    collector_number=97,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=854,
    abilities=[
        Attack(
            title='Cold Tea',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)

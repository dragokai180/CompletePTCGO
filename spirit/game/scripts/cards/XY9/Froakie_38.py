from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7204811c-e1a5-53e0-81d5-ba942a0fd496',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Froakie.Name',
    display_name='Froakie',
    searchable_by=['Froakie', 'Basic', 'Froakie'],
    subtypes=['Basic'],
    collector_number=38,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=656,
    abilities=[
        Attack(
            title='Bubble',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
    ],
)

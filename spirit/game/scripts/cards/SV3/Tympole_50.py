from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8093bd8c-f7a9-590d-9bb7-706d73df0a17',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tympole.Name',
    display_name='Tympole',
    searchable_by=['Tympole', 'Basic', 'Tympole'],
    subtypes=['Basic'],
    collector_number=50,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=535,
    abilities=[
        Attack(
            title='Screw Tail',
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)

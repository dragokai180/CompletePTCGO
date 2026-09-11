from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='901c9d7d-4374-51f3-9736-ab946124026d',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Shellder.Name',
    display_name='Shellder',
    searchable_by=['Shellder', 'Basic', 'Shellder'],
    subtypes=['Basic'],
    collector_number=90,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=90,
    abilities=[
        Attack(
            title='Shell Press',
            game_text="During your opponent's next turn, this Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)

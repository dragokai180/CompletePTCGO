from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='07b0bca5-0f68-5976-99e0-bfbb75b87b1c',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wiglett.Name',
    display_name='Wiglett',
    searchable_by=['Wiglett', 'Basic', 'Wiglett'],
    subtypes=['Basic'],
    collector_number=55,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=960,
    abilities=[
        Attack(
            title='Twisting Strike',
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)

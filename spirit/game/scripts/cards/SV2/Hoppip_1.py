from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2e2658b6-7b4a-5a88-94d0-ac94e9d877be',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hoppip.Name',
    display_name='Hoppip',
    searchable_by=['Hoppip', 'Basic', 'Hoppip'],
    subtypes=['Basic'],
    collector_number=1,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=187,
    abilities=[
        Attack(
            title='Splashing Dodge',
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)

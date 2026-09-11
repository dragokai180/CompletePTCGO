from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0297d438-ac2a-5e4c-92a3-8183adc17e6e',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Rowlet.Name',
    display_name='Rowlet',
    searchable_by=['Rowlet', 'Basic', 'Rowlet'],
    subtypes=['Basic'],
    collector_number=17,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=722,
    abilities=[
        Attack(
            title='Hide and Seek',
            game_text="Flip a coin. If heads, prevent all effects of attacks, including damage, done to this Pokémon during your opponent's next turn.",
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Tackle',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)

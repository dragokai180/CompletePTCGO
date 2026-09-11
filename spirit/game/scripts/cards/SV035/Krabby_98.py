from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7c5e5b21-6909-5a79-a52c-c67aa80de2cf',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Krabby.Name',
    display_name='Krabby',
    searchable_by=['Krabby', 'Basic', 'Krabby'],
    subtypes=['Basic'],
    collector_number=98,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=98,
    abilities=[
        Attack(
            title='Salt Water',
            game_text='Flip a coin. If heads, search your deck for up to 2 Basic Water Energy cards and attach them to this Pokémon. Then, shuffle your deck.',
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Crabhammer',
            cost={PokemonTypes.WATER: 3},
            damage=50,
        ),
    ],
)

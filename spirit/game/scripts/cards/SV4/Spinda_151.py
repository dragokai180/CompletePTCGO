from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='22d0dd0e-c9e6-5561-b391-003fbdd77b58',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Spinda.Name',
    display_name='Spinda',
    searchable_by=['Spinda', 'Basic', 'Spinda'],
    subtypes=['Basic'],
    collector_number=151,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=327,
    abilities=[
        Ability(
            title='Tangled Feet',
            game_text='If this Pokémon is Confused and is damaged by an attack, flip a coin. If heads, prevent that damage.',
            passive=standard_passive('If this Pokémon is Confused and is damaged by an attack, flip a coin. If heads, prevent that damage.'),
        ),
        Attack(
            title='Teetering Steps',
            game_text='This Pokémon is now Confused.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=standard_attack,
        ),
    ],
)

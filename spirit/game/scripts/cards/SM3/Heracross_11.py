from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='74a17627-7528-5313-b8ad-571720adfe0b',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Heracross.Name',
    display_name='Heracross',
    searchable_by=['Heracross', 'Basic', 'Heracross'],
    subtypes=['Basic'],
    collector_number=11,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=214,
    abilities=[
        Ability(
            title='Guts',
            game_text='If this Pokémon would be Knocked Out by damage from an attack, flip a coin. If heads, this Pokémon is not Knocked Out, and its remaining HP becomes 10.',
            passive=standard_passive('If this Pokémon would be Knocked Out by damage from an attack, flip a coin. If heads, this Pokémon is not Knocked Out, and its remaining HP becomes 10.'),
        ),
        Attack(
            title='Pitch',
            game_text='Your opponent switches their Active Pokémon with 1 of their Benched Pokémon.',
            cost={PokemonTypes.GRASS: 2},
            damage=50,
            effect=standard_attack,
        ),
    ],
)

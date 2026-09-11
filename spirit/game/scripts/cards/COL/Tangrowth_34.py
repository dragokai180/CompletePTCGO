from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b84891f6-114c-527e-9ea9-88866cd343bf',
    key='COL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tangrowth.Name',
    display_name='Tangrowth',
    searchable_by=['Tangrowth', 'Stage 1', 'Tangrowth'],
    subtypes=['Stage 1'],
    collector_number=34,
    set_code='COL',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tangela.Name',
    family_id=114,
    abilities=[
        Attack(
            title='Grind',
            game_text='Does 20 damage times the number of Energy attached to Tangrowth.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Plow Over',
            game_text='Flip a coin. If heads, the Defending Pokémon is now Paralyzed. If tails, put 1 Energy card attached to the Defending Pokémon in the Lost Zone.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)

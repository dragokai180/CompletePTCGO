from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d3ec67f7-21cb-593b-b52a-bfb9ea336496',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lanturn.Name',
    display_name='Lanturn',
    searchable_by=['Lanturn', 'Stage 1', 'Lanturn'],
    subtypes=['Stage 1'],
    collector_number=58,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Chinchou.Name',
    family_id=170,
    abilities=[
        Attack(
            title='Dive',
            game_text="Flip a coin. If heads, prevent all effects of attacks, including damage, done to this Pokémon during your opponent's next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=standard_attack,
        ),
        Attack(
            title='Take Down',
            game_text='This Pokémon does 20 damage to itself.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=standard_attack,
        ),
    ],
)

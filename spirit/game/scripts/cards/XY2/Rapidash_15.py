from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1ad9927b-c071-5869-bc9a-25d27ce5b501',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Rapidash.Name',
    display_name='Rapidash',
    searchable_by=['Rapidash', 'Stage 1', 'Rapidash'],
    subtypes=['Stage 1'],
    collector_number=15,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Ponyta.Name',
    family_id=77,
    abilities=[
        Attack(
            title='Agility',
            game_text="Flip a coin. If heads, prevent all effects of attacks, including damage, done to this Pokémon during your opponent's next turn.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Overrun',
            game_text="This attack does 20 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=standard_attack,
        ),
    ],
)

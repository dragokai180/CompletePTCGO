from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2746ec32-f2d9-590a-acd4-5d39c57464fb',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Rapidash.Name',
    display_name='Rapidash',
    searchable_by=['Rapidash', 'Stage 1', 'Rapidash'],
    subtypes=['Stage 1'],
    collector_number=24,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Ponyta.Name',
    family_id=77,
    abilities=[
        Attack(
            title='Overrun',
            game_text="This attack does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Flame Tail',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b1d9b19c-7e4c-5131-b59a-fbde46b87acf',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Goodra.Name',
    display_name='Goodra',
    searchable_by=['Goodra', 'Stage 2', 'Goodra'],
    subtypes=['Stage 2'],
    collector_number=60,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Sliggoo.Name',
    family_id=704,
    abilities=[
        Attack(
            title='Liquid Blow',
            game_text="This attack does 20 damage to 1 of your opponent's Pokémon for each Colorless in its Retreat Cost. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Shining Breath',
            game_text="During your opponent's next turn, this Pokémon can't be affected by any Special Conditions.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
            effect=standard_attack,
        ),
    ],
)

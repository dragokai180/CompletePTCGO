from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='66086710-2332-543d-9c47-22387d229f55',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MMewtwoEX.Name',
    display_name='M Mewtwo-EX',
    searchable_by=['M Mewtwo-EX', 'MEGA', 'EX', 'MMewtwoEX'],
    subtypes=['MEGA', 'EX'],
    collector_number=64,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.MewtwoEX.Name',
    family_id=150,
    abilities=[
        Attack(
            title='Psychic Infinity',
            game_text="This attack does 30 more damage times the amount of Energy attached to both Active Pokémon. This attack's damage isn't affected by Weakness.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

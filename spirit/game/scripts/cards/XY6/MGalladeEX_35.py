from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1cc79d5d-1c4c-5a99-9438-958001b90689',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MGalladeEX.Name',
    display_name='M Gallade-EX',
    searchable_by=['M Gallade-EX', 'MEGA', 'EX', 'MGalladeEX'],
    subtypes=['MEGA', 'EX'],
    collector_number=35,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.GalladeEX.Name',
    family_id=475,
    abilities=[
        Attack(
            title='Unwavering Blade',
            game_text="This attack does 30 damage to each of your opponent's Benched Pokémon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
            effect=standard_attack,
        ),
    ],
)

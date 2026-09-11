from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='81202dc4-d550-5d47-9c6d-47688020b93f',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MGengarEX.Name',
    display_name='M Gengar-EX',
    searchable_by=['M Gengar-EX', 'MEGA', 'EX', 'MGengarEX'],
    subtypes=['MEGA', 'EX'],
    collector_number=35,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.GengarEX.Name',
    family_id=94,
    abilities=[
        Attack(
            title='Phantom Gate',
            game_text="Choose 1 of your opponent's Pokémon's attacks and use it as this attack.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7ddac4f9-3b5d-5069-b017-f3e9e9b5d48b',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MPidgeotEX.Name',
    display_name='M Pidgeot-EX',
    searchable_by=['M Pidgeot-EX', 'MEGA', 'EX', 'MPidgeotEX'],
    subtypes=['MEGA', 'EX'],
    collector_number=65,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.PidgeotEX.Name',
    family_id=18,
    abilities=[
        Attack(
            title='Mach Cyclone',
            game_text='You may have your opponent switch his or her Active Pokémon with 1 of his or her Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=130,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='13583a61-52d9-51c7-8363-ba2ccb331884',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MGardevoirEX.Name',
    display_name='M Gardevoir-EX',
    searchable_by=['M Gardevoir-EX', 'MEGA', 'EX', 'MGardevoirEX'],
    subtypes=['MEGA', 'EX'],
    collector_number=106,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=210,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.GardevoirEX.Name',
    family_id=282,
    abilities=[
        Attack(
            title='Brilliant Arrow',
            game_text='This attack does 30 damage times the amount of Fairy Energy attached to all of your Pokémon.',
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)

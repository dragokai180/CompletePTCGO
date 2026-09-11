from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='26a9e4aa-68c0-5247-9b09-205c7016d12c',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MGlalieEX.Name',
    display_name='M Glalie-EX',
    searchable_by=['M Glalie-EX', 'MEGA', 'EX', 'MGlalieEX'],
    subtypes=['MEGA', 'EX'],
    collector_number=35,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.GlalieEX.Name',
    family_id=362,
    abilities=[
        Attack(
            title='Cryo Mouth',
            game_text='If this Pokémon has 10 or more damage counters on it, this attack does 150 more damage.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

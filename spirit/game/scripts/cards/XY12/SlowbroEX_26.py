from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='658a66f7-be51-564e-8636-ed408773128a',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.SlowbroEX.Name',
    display_name='Slowbro-EX',
    searchable_by=['Slowbro-EX', 'Basic', 'EX', 'SlowbroEX'],
    subtypes=['Basic', 'EX'],
    collector_number=26,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=80,
    abilities=[
        Attack(
            title='Slack Off',
            game_text="Heal 60 damage from this Pokémon. This Pokémon can't attack during your next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Flash Splash',
            cost={PokemonTypes.WATER: 3},
            damage=100,
        ),
    ],
)

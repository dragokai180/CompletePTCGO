from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='565f2e1e-3ff7-532a-9749-d303a682e74f',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.CameruptEX.Name',
    display_name='Camerupt-EX',
    searchable_by=['Camerupt-EX', 'Basic', 'EX', 'CameruptEX'],
    subtypes=['Basic', 'EX'],
    collector_number=29,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=323,
    abilities=[
        Attack(
            title='Tumbling Attack',
            game_text='Flip a coin. If heads, this attack does 30 more damage.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Explosive Jet',
            game_text='Discard as many Fire Energy attached to your Pokémon as you like. This attack does 50 damage times the number of Energy cards you discarded.',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)

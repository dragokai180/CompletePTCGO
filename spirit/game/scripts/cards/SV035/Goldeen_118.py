from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='99cf1e7a-a244-5792-99e7-826d63c9aab1',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Goldeen.Name',
    display_name='Goldeen',
    searchable_by=['Goldeen', 'Basic', 'Goldeen'],
    subtypes=['Basic'],
    collector_number=118,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=118,
    abilities=[
        Attack(
            title='Triple Strike',
            game_text='Flip 3 coins. This attack does 10 damage for each heads.',
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Sprinkle Water',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)

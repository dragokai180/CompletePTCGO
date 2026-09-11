from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0bc6326a-afba-502c-b770-6b2d6b321370',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.SteelixEX.Name',
    display_name='Steelix-EX',
    searchable_by=['Steelix-EX', 'Basic', 'EX', 'SteelixEX'],
    subtypes=['Basic', 'EX'],
    collector_number=67,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=208,
    abilities=[
        Attack(
            title='Wild Edge',
            game_text='You may do 50 more damage. If you do, this Pokémon does 20 damage to itself.',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Iron Tail',
            game_text='Flip a coin until you get tails. This attack does 100 damage times the number of heads.',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 4},
            damage=100,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='726f929a-4fd5-57bc-b6dd-bfdc302e0130',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kangaskhanex.Name',
    display_name='Kangaskhan ex',
    searchable_by=['Kangaskhan ex', 'Basic', 'ex', 'Kangaskhanex'],
    subtypes=['Basic', 'ex'],
    collector_number=115,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=230,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=115,
    abilities=[
        Attack(
            title='Triple Draw',
            game_text='Draw 3 cards.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Incessant Punching',
            game_text='Flip 4 coins. This attack does 100 damage for each heads.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='82fcf1da-1c63-56dc-8673-6b4d6e0a25ce',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.KingdraEX.Name',
    display_name='Kingdra-EX',
    searchable_by=['Kingdra-EX', 'Basic', 'EX', 'KingdraEX'],
    subtypes=['Basic', 'EX'],
    collector_number=73,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=230,
    abilities=[
        Attack(
            title='Big Storm',
            game_text='Discard any Stadium card in play.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Dragon Trail',
            game_text='This attack does 30 more damage for each basic Lightning Energy attached to this Pokémon.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

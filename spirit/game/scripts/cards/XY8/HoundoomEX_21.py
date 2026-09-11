from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c6c9d67c-848a-5637-97da-8f8878c1e741',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.HoundoomEX.Name',
    display_name='Houndoom-EX',
    searchable_by=['Houndoom-EX', 'Basic', 'EX', 'HoundoomEX'],
    subtypes=['Basic', 'EX'],
    collector_number=21,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=229,
    abilities=[
        Attack(
            title='Melting Horn',
            game_text="Discard the top 2 cards of your opponent's deck.",
            cost={PokemonTypes.FIRE: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Grand Flame',
            game_text='Attach a Fire Energy card from your discard pile to 1 of your Benched Pokémon.',
            cost={PokemonTypes.FIRE: 2},
            damage=50,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3c31c80a-7218-5b14-afe9-df18ec63c089',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.TogekissEX.Name',
    display_name='Togekiss-EX',
    searchable_by=['Togekiss-EX', 'Basic', 'EX', 'TogekissEX'],
    subtypes=['Basic', 'EX'],
    collector_number=83,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=468,
    abilities=[
        Attack(
            title='Mighty Wind',
            game_text='You may attach an Energy card from your hand to 1 of your Benched Pokémon.',
            cost={PokemonTypes.FAIRY: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Hurricane Wing',
            game_text='Flip 4 coins. This attack does 50 damage times the number of heads.',
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)

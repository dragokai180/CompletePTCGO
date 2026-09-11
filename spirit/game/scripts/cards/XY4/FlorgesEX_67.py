from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='60139a90-8c60-56bf-be4c-864ef0479127',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.FlorgesEX.Name',
    display_name='Florges-EX',
    searchable_by=['Florges-EX', 'Basic', 'EX', 'FlorgesEX'],
    subtypes=['Basic', 'EX'],
    collector_number=67,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=160,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=671,
    abilities=[
        Attack(
            title='Lead',
            game_text='Search your deck for a Supporter card, reveal it, and put it into your hand. Shuffle your deck afterward.',
            cost={PokemonTypes.FAIRY: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Bright Garden',
            game_text='This attack does 20 damage times the number of Grass Pokémon and Fairy Pokémon you have in play.',
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)

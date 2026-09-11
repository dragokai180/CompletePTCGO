from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='396fed67-66bf-5c52-b0ef-074ad11fe90a',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.LugiaEX.Name',
    display_name='Lugia-EX',
    searchable_by=['Lugia-EX', 'Basic', 'EX', 'LugiaEX'],
    subtypes=['Basic', 'EX'],
    collector_number=68,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=249,
    abilities=[
        Attack(
            title='Aero Ball',
            game_text='This attack does 20 damage times the amount of Energy attached to both Active Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Deep Hurricane',
            game_text='If there is any Stadium card in play, this attack does 70 more damage. Then, discard that Stadium card.',
            cost={PokemonTypes.COLORLESS: 4},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

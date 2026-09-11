from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='91db996a-d27c-55c4-b2c1-9d4c8c4eeeff',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Moltres.Name',
    display_name='Moltres',
    searchable_by=['Moltres', 'Basic', 'Moltres'],
    subtypes=['Basic'],
    collector_number=9,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=146,
    abilities=[
        Attack(
            title='Combustion',
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
        Attack(
            title='Flying Flare',
            game_text='You may do 40 more damage. If you do, this Pokémon does 20 damage to itself.',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

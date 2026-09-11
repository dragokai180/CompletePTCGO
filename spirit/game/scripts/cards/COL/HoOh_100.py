from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='eca5eb27-540f-5be3-ae59-36caff8702b9',
    key='COL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.HoOh.Name',
    display_name='Ho-Oh',
    searchable_by=['Ho-Oh', 'Basic', 'HoOh'],
    subtypes=['Basic'],
    collector_number=100,
    set_code='COL',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    attributes={200790: {'type': 'string', 'value': 'SL5'}},
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=250,
    abilities=[
        Attack(
            title='Combustion',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title='Scorching Wing',
            game_text='Flip a coin. If tails, discard all Fire Energy attached to Ho-Oh.',
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=standard_attack,
        ),
    ],
)

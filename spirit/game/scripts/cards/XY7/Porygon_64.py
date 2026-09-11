from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='42d15757-0ad3-5d95-b541-a845fb6279ab',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Porygon.Name',
    display_name='Porygon',
    searchable_by=['Porygon', 'Basic', 'Porygon'],
    subtypes=['Basic'],
    collector_number=64,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=137,
    abilities=[
        Attack(
            title='Data Check',
            game_text='Look through your deck. Shuffle your deck afterward.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Sharpen',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)

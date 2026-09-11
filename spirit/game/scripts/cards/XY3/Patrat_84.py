from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fe77e47b-363b-5605-adc0-33394cc78cd5',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Patrat.Name',
    display_name='Patrat',
    searchable_by=['Patrat', 'Basic', 'Patrat'],
    subtypes=['Basic'],
    collector_number=84,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=504,
    abilities=[
        Attack(
            title='Safety Check',
            game_text='Look at 1 of your face-down Prize cards.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)

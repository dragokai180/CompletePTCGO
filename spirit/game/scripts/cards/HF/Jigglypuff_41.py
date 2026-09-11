from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c87af598-fdb5-5876-84c1-3965a9f05b08',
    key='HF',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Jigglypuff.Name',
    display_name='Jigglypuff',
    searchable_by=['Jigglypuff', 'Basic', 'Jigglypuff'],
    subtypes=['Basic'],
    collector_number=41,
    set_code='HF',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=39,
    abilities=[
        Attack(
            title='Singing Voice',
            cost={PokemonTypes.FAIRY: 1},
            damage=10,
        ),
        Attack(
            title='Rollout',
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)

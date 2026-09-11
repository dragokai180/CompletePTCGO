from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='22c8a9b2-5c6a-5fe6-abfb-500ca81e4c42',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Salandit.Name',
    display_name='Salandit',
    searchable_by=['Salandit', 'Basic', 'Salandit'],
    subtypes=['Basic'],
    collector_number=98,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=757,
    abilities=[
        Attack(
            title='Suffocating Gas',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
        Attack(
            title='Gnaw',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)

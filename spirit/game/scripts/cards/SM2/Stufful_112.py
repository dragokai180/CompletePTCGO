from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='358a1884-1166-5323-8474-6746c0effe8c',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Stufful.Name',
    display_name='Stufful',
    searchable_by=['Stufful', 'Basic', 'Stufful'],
    subtypes=['Basic'],
    collector_number=112,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=759,
    abilities=[
        Attack(
            title='Tackle',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Hammer In',
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
    ],
)

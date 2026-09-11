from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='aff4dd46-a57c-59ed-8eb6-3653c3f3a6fe',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Abra.Name',
    display_name='Abra',
    searchable_by=['Abra', 'Basic', 'Abra'],
    subtypes=['Basic'],
    collector_number=63,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=63,
    abilities=[
        Attack(
            title='Psyshot',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4782cf40-7e37-59f1-b803-d0d25f860577',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Flittle.Name',
    display_name='Flittle',
    searchable_by=['Flittle', 'Basic', 'Flittle'],
    subtypes=['Basic'],
    collector_number=101,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=955,
    abilities=[
        Attack(
            title='Spinning Attack',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)

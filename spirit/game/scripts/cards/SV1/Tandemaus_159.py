from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='161ad7d3-5727-5a1a-b61e-017bdf3b11c8',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tandemaus.Name',
    display_name='Tandemaus',
    searchable_by=['Tandemaus', 'Basic', 'Tandemaus'],
    subtypes=['Basic'],
    collector_number=159,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=924,
    abilities=[
        Attack(
            title='Gnaw',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)

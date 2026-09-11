from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ccdc2473-eac9-5e35-9372-7d71ea05e79c',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ralts.Name',
    display_name='Ralts',
    searchable_by=['Ralts', 'Basic', 'Ralts'],
    subtypes=['Basic'],
    collector_number=84,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=280,
    abilities=[
        Attack(
            title='Psyshot',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)

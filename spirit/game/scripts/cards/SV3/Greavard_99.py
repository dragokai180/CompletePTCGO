from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9e99ceac-1f6e-503d-9d48-cbf95691d301',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Greavard.Name',
    display_name='Greavard',
    searchable_by=['Greavard', 'Basic', 'Greavard'],
    subtypes=['Basic'],
    collector_number=99,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=971,
    abilities=[
        Attack(
            title='Gnaw',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
        Attack(
            title='Spooky Shot',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)

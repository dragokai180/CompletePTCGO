from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='89859cf9-bbee-573b-bbee-a370ce2ddade',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Crabrawler.Name',
    display_name='Crabrawler',
    searchable_by=['Crabrawler', 'Basic', 'Crabrawler'],
    subtypes=['Basic'],
    collector_number=114,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=739,
    abilities=[
        Attack(
            title='Knuckle Punch',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title='Magnum Punch',
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)

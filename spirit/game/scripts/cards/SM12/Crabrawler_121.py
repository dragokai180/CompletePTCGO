from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bdf57828-e17e-51ae-927e-1e87e0e9c9e4',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Crabrawler.Name',
    display_name='Crabrawler',
    searchable_by=['Crabrawler', 'Basic', 'Crabrawler'],
    subtypes=['Basic'],
    collector_number=121,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=739,
    abilities=[
        Attack(
            title='Jab',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Confront',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)

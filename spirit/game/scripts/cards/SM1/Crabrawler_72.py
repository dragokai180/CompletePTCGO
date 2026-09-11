from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cd8ca43a-6b79-5572-b42e-49f0fc52c5e5',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Crabrawler.Name',
    display_name='Crabrawler',
    searchable_by=['Crabrawler', 'Basic', 'Crabrawler'],
    subtypes=['Basic'],
    collector_number=72,
    set_code='SM1',
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
            title='Punch',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title='Crabhammer',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)

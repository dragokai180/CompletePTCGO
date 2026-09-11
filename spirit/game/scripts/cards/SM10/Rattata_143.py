from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='16e4aab5-d3f8-5a89-ad5c-57132e139ff0',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Rattata.Name',
    display_name='Rattata',
    searchable_by=['Rattata', 'Basic', 'Rattata'],
    subtypes=['Basic'],
    collector_number=143,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=19,
    abilities=[
        Attack(
            title='Gnaw',
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)

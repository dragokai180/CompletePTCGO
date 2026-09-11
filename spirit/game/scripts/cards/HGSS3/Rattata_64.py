from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='af646ce4-2255-5620-acf6-f8b454c51d6e',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Rattata.Name',
    display_name='Rattata',
    searchable_by=['Rattata', 'Basic', 'Rattata'],
    subtypes=['Basic'],
    collector_number=64,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=40,
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
            damage=20,
        ),
    ],
)

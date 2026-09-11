from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cd1117cd-1903-56b3-9e10-8aadb1c3cba9',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name',
    display_name='Growlithe',
    searchable_by=['Growlithe', 'Basic', 'Growlithe'],
    subtypes=['Basic'],
    collector_number=65,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=58,
    abilities=[
        Attack(
            title='Bite',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Combustion',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)

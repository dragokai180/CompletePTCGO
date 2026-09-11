from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6e129ca8-1d1a-5bc9-9b78-241a2937f939',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cyndaquil.Name',
    display_name='Cyndaquil',
    searchable_by=['Cyndaquil', 'Basic', 'Cyndaquil'],
    subtypes=['Basic'],
    collector_number=61,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=155,
    abilities=[
        Attack(
            title='Beat',
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
        Attack(
            title='Flare',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6d51956d-2979-57d4-b302-2e4c724c59c0',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Grimer.Name',
    display_name='Grimer',
    searchable_by=['Grimer', 'Basic', 'Grimer'],
    subtypes=['Basic'],
    collector_number=62,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=88,
    abilities=[
        Attack(
            title='Pound',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)

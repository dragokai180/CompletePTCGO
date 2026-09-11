from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='48ca6f92-9e5d-53ac-b45e-ce6ba859c7c4',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Solosis.Name',
    display_name='Solosis',
    searchable_by=['Solosis', 'Basic', 'Solosis'],
    subtypes=['Basic'],
    collector_number=33,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=577,
    abilities=[
        Attack(
            title='Mini Link',
            game_text='If Solosis is on your Bench, this attack does 30 more damage.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

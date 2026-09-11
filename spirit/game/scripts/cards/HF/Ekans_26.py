from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='66276e24-8b92-5ca4-b8bf-56f0c13bde67',
    key='HF',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ekans.Name',
    display_name='Ekans',
    searchable_by=['Ekans', 'Basic', 'Ekans'],
    subtypes=['Basic'],
    collector_number=26,
    set_code='HF',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=23,
    abilities=[
        Attack(
            title='Tail Whap',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)

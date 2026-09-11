from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5cddebd2-eb94-5f0c-95e1-1f39dea28f2b',
    key='HF',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Geodude.Name',
    display_name='Geodude',
    searchable_by=['Geodude', 'Basic', 'Geodude'],
    subtypes=['Basic'],
    collector_number=33,
    set_code='HF',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=74,
    abilities=[
        Attack(
            title='Tackle',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)

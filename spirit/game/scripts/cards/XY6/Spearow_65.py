from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fa421d80-6b9e-5e66-9700-cd384b9178f1',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Spearow.Name',
    display_name='Spearow',
    searchable_by=['Spearow', 'Basic', 'Spearow'],
    subtypes=['Basic'],
    collector_number=65,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=21,
    abilities=[
        Attack(
            title='Peck',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)

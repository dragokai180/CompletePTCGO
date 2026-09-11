from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='efb25156-c15f-59ce-818a-613466786b85',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Quagsire.Name',
    display_name='Quagsire',
    searchable_by=['Quagsire', 'Stage 1', 'Quagsire'],
    subtypes=['Stage 1'],
    collector_number=97,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Wooper.Name',
    family_id=194,
    abilities=[
        Attack(
            title='Water Gun',
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title='Surf',
            cost={PokemonTypes.WATER: 3},
            damage=120,
        ),
    ],
)

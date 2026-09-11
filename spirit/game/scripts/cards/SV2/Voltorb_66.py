from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8c725fbc-3f42-5980-a006-ee66b085174b',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name',
    display_name='Voltorb',
    searchable_by=['Voltorb', 'Basic', 'Voltorb'],
    subtypes=['Basic'],
    collector_number=66,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=100,
    abilities=[
        Attack(
            title='Lightning Ball',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
        Attack(
            title='Rollout',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)

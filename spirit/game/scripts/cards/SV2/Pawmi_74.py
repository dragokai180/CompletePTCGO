from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3e71d6de-02dd-5666-9bad-dbb0f51052d7',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pawmi.Name',
    display_name='Pawmi',
    searchable_by=['Pawmi', 'Basic', 'Pawmi'],
    subtypes=['Basic'],
    collector_number=74,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=921,
    abilities=[
        Attack(
            title='Static Shock',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
        ),
    ],
)

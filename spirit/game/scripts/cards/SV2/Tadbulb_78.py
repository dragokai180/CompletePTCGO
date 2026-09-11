from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4a550ce5-90a4-5e86-b377-65a83e519525',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tadbulb.Name',
    display_name='Tadbulb',
    searchable_by=['Tadbulb', 'Basic', 'Tadbulb'],
    subtypes=['Basic'],
    collector_number=78,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=938,
    abilities=[
        Attack(
            title='Stampede',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Static Shock',
            cost={PokemonTypes.LIGHTNING: 2},
            damage=30,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d663abfb-47c7-53b6-9b3f-316b0309c46b',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Meltan.Name',
    display_name='Meltan',
    searchable_by=['Meltan', 'Basic', 'Meltan'],
    subtypes=['Basic'],
    collector_number=152,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=808,
    abilities=[
        Attack(
            title='Melt',
            cost={PokemonTypes.METAL: 1},
            damage=20,
        ),
    ],
)

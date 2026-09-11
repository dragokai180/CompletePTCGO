from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='54811ea6-29ec-5304-ad7d-1549168faa7e',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Clauncher.Name',
    display_name='Clauncher',
    searchable_by=['Clauncher', 'Basic', 'Clauncher'],
    subtypes=['Basic'],
    collector_number=49,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=692,
    abilities=[
        Attack(
            title='Vise Grip',
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)

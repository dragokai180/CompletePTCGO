from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3dea9a50-ad46-5b35-9883-f2283ac6d0bd',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Spoink.Name',
    display_name='Spoink',
    searchable_by=['Spoink', 'Basic', 'Spoink'],
    subtypes=['Basic'],
    collector_number=90,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=325,
    abilities=[
        Attack(
            title='Splash',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
        Attack(
            title='Ram',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)

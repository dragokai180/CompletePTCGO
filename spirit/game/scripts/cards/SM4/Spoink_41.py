from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fadec1e8-18b6-52b0-a06a-2adb397e50a2',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Spoink.Name',
    display_name='Spoink',
    searchable_by=['Spoink', 'Basic', 'Spoink'],
    subtypes=['Basic'],
    collector_number=41,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=325,
    abilities=[
        Attack(
            title='Splash',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)

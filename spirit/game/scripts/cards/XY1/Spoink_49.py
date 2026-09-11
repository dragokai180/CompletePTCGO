from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='197b15bb-2cd1-58ed-a35b-960bfde8fb7f',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Spoink.Name',
    display_name='Spoink',
    searchable_by=['Spoink', 'Basic', 'Spoink'],
    subtypes=['Basic'],
    collector_number=49,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=325,
    abilities=[
        Attack(
            title='Splash',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='60c03284-d32f-53d6-9e9e-edc925bc9d96',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Zweilous.Name',
    display_name='Zweilous',
    searchable_by=['Zweilous', 'Stage 1', 'Zweilous'],
    subtypes=['Stage 1'],
    collector_number=98,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Deino.Name',
    family_id=633,
    abilities=[
        Attack(
            title='Bite',
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
        ),
        Attack(
            title='Hammer In',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)

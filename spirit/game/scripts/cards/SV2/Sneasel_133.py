from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1c9fb991-9dbc-5c10-ba79-e594c8a0a3ad',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sneasel.Name',
    display_name='Sneasel',
    searchable_by=['Sneasel', 'Basic', 'Sneasel'],
    subtypes=['Basic'],
    collector_number=133,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=215,
    abilities=[
        Attack(
            title='Dig Claws',
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
        ),
    ],
)

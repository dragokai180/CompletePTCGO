from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3aa32112-fda6-53cf-a403-12d8fbf5cf31',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Snover.Name',
    display_name='Snover',
    searchable_by=['Snover', 'Basic', 'Snover'],
    subtypes=['Basic'],
    collector_number=10,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=459,
    abilities=[
        Attack(
            title='Corkscrew Punch',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)

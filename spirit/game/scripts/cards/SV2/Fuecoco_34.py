from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='94866ec1-0e20-5a16-9f5e-18c4bfd29f0b',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Fuecoco.Name',
    display_name='Fuecoco',
    searchable_by=['Fuecoco', 'Basic', 'Fuecoco'],
    subtypes=['Basic'],
    collector_number=34,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=909,
    abilities=[
        Attack(
            title='Tackle',
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
    ],
)

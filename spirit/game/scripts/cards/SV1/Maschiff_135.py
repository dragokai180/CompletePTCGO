from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0f571207-1c73-5695-bc0f-8ae9f5797dcb',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Maschiff.Name',
    display_name='Maschiff',
    searchable_by=['Maschiff', 'Basic', 'Maschiff'],
    subtypes=['Basic'],
    collector_number=135,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=942,
    abilities=[
        Attack(
            title='Rear Kick',
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
        Attack(
            title='Darkness Fang',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)

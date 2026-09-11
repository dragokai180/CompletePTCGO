from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e8c747d0-924a-5734-9d0c-36f30f924998',
    key='SV045',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Phanpy.Name',
    display_name='Phanpy',
    searchable_by=['Phanpy', 'Basic', 'Phanpy'],
    subtypes=['Basic'],
    collector_number=48,
    set_code='SV045',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=231,
    abilities=[
        Attack(
            title='Strength',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title='Rolling Tackle',
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)

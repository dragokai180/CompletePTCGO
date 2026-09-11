from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8fe07d4e-0dc9-5051-8340-59e4e468e30a',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Zangoose.Name',
    display_name='Zangoose',
    searchable_by=['Zangoose', 'Basic', 'Zangoose'],
    subtypes=['Basic'],
    collector_number=146,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=335,
    abilities=[
        Attack(
            title='Slash',
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)

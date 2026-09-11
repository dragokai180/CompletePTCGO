from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='01af3348-55d1-502d-9004-ec53a2567f35',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Krabby.Name',
    display_name='Krabby',
    searchable_by=['Krabby', 'Basic', 'Krabby'],
    subtypes=['Basic'],
    collector_number=46,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=98,
    abilities=[
        Attack(
            title='Stampede',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Vice Grip',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)

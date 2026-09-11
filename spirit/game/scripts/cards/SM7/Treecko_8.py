from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ba97c322-7b7e-5c48-b7ad-726a8322cfc5',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Treecko.Name',
    display_name='Treecko',
    searchable_by=['Treecko', 'Basic', 'Treecko'],
    subtypes=['Basic'],
    collector_number=8,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=252,
    abilities=[
        Attack(
            title='Smack',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
        Attack(
            title='Tail Whap',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bb616039-cf00-57f6-ab7f-82c09f45d69d',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mudkip.Name',
    display_name='Mudkip',
    searchable_by=['Mudkip', 'Basic', 'Mudkip'],
    subtypes=['Basic'],
    collector_number=33,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=258,
    abilities=[
        Attack(
            title='Tackle',
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title='Wave Splash',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)

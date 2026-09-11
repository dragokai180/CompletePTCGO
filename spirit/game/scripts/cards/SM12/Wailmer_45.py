from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a4070bdb-2775-550e-987e-fe5186ea5085',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wailmer.Name',
    display_name='Wailmer',
    searchable_by=['Wailmer', 'Basic', 'Wailmer'],
    subtypes=['Basic'],
    collector_number=45,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=320,
    abilities=[
        Attack(
            title='Wave Splash',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)

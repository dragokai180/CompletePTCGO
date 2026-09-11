from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='391080af-521a-5186-8b57-a0ecfbba9ba1',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dewpider.Name',
    display_name='Dewpider',
    searchable_by=['Dewpider', 'Basic', 'Dewpider'],
    subtypes=['Basic'],
    collector_number=48,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=751,
    abilities=[
        Attack(
            title='Rain Splash',
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title='Bite',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)

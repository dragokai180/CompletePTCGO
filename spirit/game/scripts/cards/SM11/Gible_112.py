from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='876bd241-d367-5591-abb5-a07d2f2f6563',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gible.Name',
    display_name='Gible',
    searchable_by=['Gible', 'Basic', 'Gible'],
    subtypes=['Basic'],
    collector_number=112,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=443,
    abilities=[
        Attack(
            title='Stampede',
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
        Attack(
            title='Headbutt Bounce',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)

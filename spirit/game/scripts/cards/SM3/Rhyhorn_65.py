from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c5bbe39a-8995-5b5d-89bc-9d04a184baff',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Rhyhorn.Name',
    display_name='Rhyhorn',
    searchable_by=['Rhyhorn', 'Basic', 'Rhyhorn'],
    subtypes=['Basic'],
    collector_number=65,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=111,
    abilities=[
        Attack(
            title='Lunge Out',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title='Horn Drill',
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)

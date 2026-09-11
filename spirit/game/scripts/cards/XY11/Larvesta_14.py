from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f7ae1769-32a3-5f5e-9d33-8087df84e215',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Larvesta.Name',
    display_name='Larvesta',
    searchable_by=['Larvesta', 'Basic', 'Larvesta'],
    subtypes=['Basic'],
    collector_number=14,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=636,
    abilities=[
        Attack(
            title='Bug Bite',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)

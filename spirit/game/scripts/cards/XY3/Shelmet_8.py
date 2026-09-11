from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3b008715-3d9f-5ad2-8b6e-94b14e599fca',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Shelmet.Name',
    display_name='Shelmet',
    searchable_by=['Shelmet', 'Basic', 'Shelmet'],
    subtypes=['Basic'],
    collector_number=8,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=616,
    abilities=[
        Attack(
            title='Jump On',
            game_text='Flip a coin. If heads, this attack does 10 more damage.',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

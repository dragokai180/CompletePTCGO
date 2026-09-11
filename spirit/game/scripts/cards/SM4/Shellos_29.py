from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='eae264f6-2014-5cf9-8148-444a11cb1f21',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Shellos.Name',
    display_name='Shellos',
    searchable_by=['Shellos', 'Basic', 'Shellos'],
    subtypes=['Basic'],
    collector_number=29,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=422,
    abilities=[
        Attack(
            title='Regeneration',
            game_text='Heal 30 damage from this Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Mud-Slap',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)

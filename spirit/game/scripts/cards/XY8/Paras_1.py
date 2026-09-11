from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='67001eb0-1ef6-5dd2-a80b-c6bfd3d810a8',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Paras.Name',
    display_name='Paras',
    searchable_by=['Paras', 'Basic', 'Paras'],
    subtypes=['Basic'],
    collector_number=1,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=46,
    abilities=[
        Attack(
            title='Blot',
            game_text='Heal 10 damage from this Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)

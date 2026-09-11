from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d1edb5e7-9d3b-5247-934a-ee319b3de706',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Chikorita.Name',
    display_name='Chikorita',
    searchable_by=['Chikorita', 'Basic', 'Chikorita'],
    subtypes=['Basic'],
    collector_number=6,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=152,
    abilities=[
        Attack(
            title='Mini Drain',
            game_text='Heal 10 damage from this Pokémon.',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)

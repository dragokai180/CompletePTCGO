from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4f2b8f81-19e5-5d2b-bd44-d086fdd4b435',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Venonat.Name',
    display_name='Venonat',
    searchable_by=['Venonat', 'Basic', 'Venonat'],
    subtypes=['Basic'],
    collector_number=1,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=48,
    abilities=[
        Attack(
            title='Stun Spore',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)

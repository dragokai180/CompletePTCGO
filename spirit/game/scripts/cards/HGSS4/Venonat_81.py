from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='46b9b742-3444-53b3-b4f2-150307a4964f',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Venonat.Name',
    display_name='Venonat',
    searchable_by=['Venonat', 'Basic', 'Venonat'],
    subtypes=['Basic'],
    collector_number=81,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=48,
    abilities=[
        Attack(
            title='Leech Life',
            game_text='Remove from Venonat the number of damage counters equal to the damage you did to the Defending Pokémon.',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=standard_attack,
        ),
        Attack(
            title='Tackle',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)

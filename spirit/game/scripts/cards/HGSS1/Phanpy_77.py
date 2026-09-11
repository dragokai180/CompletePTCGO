from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1c54cf5b-8777-50df-8b2a-1f5d65b4a401',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Phanpy.Name',
    display_name='Phanpy',
    searchable_by=['Phanpy', 'Basic', 'Phanpy'],
    subtypes=['Basic'],
    collector_number=77,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    family_id=231,
    abilities=[
        Attack(
            title='Flail',
            game_text='Does 10 damage times the number of damage counters on Phanpy.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)

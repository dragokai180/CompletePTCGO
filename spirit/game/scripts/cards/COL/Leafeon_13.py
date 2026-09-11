from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='adc551fd-1bbd-5b08-841e-350c4829d3bd',
    key='COL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Leafeon.Name',
    display_name='Leafeon',
    searchable_by=['Leafeon', 'Stage 1', 'Leafeon'],
    subtypes=['Stage 1'],
    collector_number=13,
    set_code='COL',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name',
    family_id=133,
    abilities=[
        Attack(
            title='Miasma Wind',
            game_text='Does 50 damage times the number of Special Conditions affecting the Defending Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Sooting Scent',
            game_text='The Defending Pokémon is now Asleep.',
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)

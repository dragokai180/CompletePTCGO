from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='80b9efa0-649d-5dc1-adf1-42a1cd75bec0',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Leafeon.Name',
    display_name='Leafeon',
    searchable_by=['Leafeon', 'Stage 1', 'Leafeon'],
    subtypes=['Stage 1'],
    collector_number=17,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Rare,
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
            game_text='Does 50 damage damage times the number of Special Conditions affecting the Defending Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Soothing Scent',
            game_text='The Defending Pokémon is now Asleep.',
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)

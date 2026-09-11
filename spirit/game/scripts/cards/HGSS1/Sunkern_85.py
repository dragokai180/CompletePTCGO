from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='384ba8b5-6fae-5c29-8b20-46a5f93c7e4d',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sunkern.Name',
    display_name='Sunkern',
    searchable_by=['Sunkern', 'Basic', 'Sunkern'],
    subtypes=['Basic'],
    collector_number=85,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    family_id=191,
    abilities=[
        Attack(
            title='Cure Kernels',
            game_text='Remove 2 damage counters from 1 of your Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Seed Bomb',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)

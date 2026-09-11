from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6e0475ee-2185-57f0-bc15-828351a3e175',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Metapod.Name',
    display_name='Metapod',
    searchable_by=['Metapod', 'Stage 1', 'Metapod'],
    subtypes=['Stage 1'],
    collector_number=46,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Caterpie.Name',
    family_id=10,
    abilities=[
        Ability(
            title='Green Shield',
            game_text='Each of your Grass Pokémon has no Weakness.',
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive('Each of your Grass Pokémon has no Weakness.'),
        ),
        Attack(
            title='Sharpen',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)

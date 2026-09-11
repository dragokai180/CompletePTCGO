from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='40c412be-a53f-5d70-85b0-c8b26461de78',
    key='DM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Shelgon.Name',
    display_name='Shelgon',
    searchable_by=['Shelgon', 'Stage 1', 'Shelgon'],
    subtypes=['Stage 1'],
    collector_number=43,
    set_code='DM',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Bagon.Name',
    family_id=371,
    abilities=[
        Ability(
            title='Energy Guard',
            game_text='If this Pokémon has any basic Energy attached to it, it takes 20 less damage from attacks (after applying Weakness and Resistance).',
            passive=standard_passive('If this Pokémon has any basic Energy attached to it, it takes 20 less damage from attacks (after applying Weakness and Resistance).'),
        ),
        Attack(
            title='Rollout',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)

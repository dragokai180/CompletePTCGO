from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='df5c6f6d-ae62-5e7d-9dfe-64292b207c45',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sliggoo.Name',
    display_name='Sliggoo',
    searchable_by=['Sliggoo', 'Stage 1', 'Sliggoo'],
    subtypes=['Stage 1'],
    collector_number=73,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Goomy.Name',
    family_id=704,
    abilities=[
        Attack(
            title='Gooey',
            game_text='Heal 30 damage from this Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Gentle Slap',
            cost={PokemonTypes.WATER: 1, PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)

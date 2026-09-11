from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bd210beb-876a-5e22-a67c-eb45aeabf5cf',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Silcoon.Name',
    display_name='Silcoon',
    searchable_by=['Silcoon', 'Stage 1', 'Silcoon'],
    subtypes=['Stage 1'],
    collector_number=25,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Wurmple.Name',
    family_id=265,
    abilities=[
        Attack(
            title='Cocoon Collector',
            game_text='Search your deck for up to 4 in any combination of Silcoon and Cascoon and put them onto your Bench. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Rolling Tackle',
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9fd0f6e0-127c-5b20-aa62-8ec24721253e',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Grotle.Name',
    display_name='Grotle',
    searchable_by=['Grotle', 'Stage 1', 'Grotle'],
    subtypes=['Stage 1'],
    collector_number=8,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Turtwig.Name',
    family_id=387,
    abilities=[
        Attack(
            title='Mega Drain',
            game_text='Heal 30 damage from this Pokémon.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Razor Leaf',
            cost={PokemonTypes.GRASS: 3, PokemonTypes.COLORLESS: 1},
            damage=80,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e289bc2a-002d-500c-993a-4d19daeedc3b',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name',
    display_name='Gloom',
    searchable_by=['Gloom', 'Stage 1', 'Gloom'],
    subtypes=['Stage 1'],
    collector_number=3,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Oddish.Name',
    family_id=43,
    abilities=[
        Attack(
            title='Sleep Powder',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)

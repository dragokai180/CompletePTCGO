from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f005164e-f0fc-5ddc-8674-9d138ffced25',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Leavanny.Name',
    display_name='Leavanny',
    searchable_by=['Leavanny', 'Stage 2', 'Leavanny'],
    subtypes=['Stage 2'],
    collector_number=7,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Swadloon.Name',
    family_id=540,
    abilities=[
        Attack(
            title='Coordinate',
            game_text='Choose up to 2 of your Benched Pokémon that have no Pokémon Tools attached to them. For each of those Pokémon, search your deck for a Pokémon Tool card, and attach it to that Pokémon. Shuffle your deck afterward.',
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Leaf Storm',
            game_text='Heal 20 damage from each of your Grass Pokémon.',
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5dca825b-872d-52e4-b840-ce040e058afc',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bellossom.Name',
    display_name='Bellossom',
    searchable_by=['Bellossom', 'Stage 2', 'Bellossom'],
    subtypes=['Stage 2'],
    collector_number=4,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name',
    family_id=43,
    abilities=[
        Attack(
            title='Windmill',
            game_text='Switch this Pokémon with 1 of your Benched Pokémon.',
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Flower Tornado',
            game_text='Move as many Grass Energy attached to your Pokémon to your other Pokémon in any way you like.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=standard_attack,
        ),
    ],
)

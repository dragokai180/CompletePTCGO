from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e161787a-eb3d-5606-9f50-d81ea9144054',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Torracat.Name',
    display_name='Torracat',
    searchable_by=['Torracat', 'Stage 1', 'Torracat'],
    subtypes=['Stage 1'],
    collector_number=25,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Litten.Name',
    family_id=725,
    abilities=[
        Attack(
            title='Fury Swipes',
            game_text='Flip 3 coins. This attack does 20 damage for each heads.',
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Flamethrower',
            game_text='Discard an Energy from this Pokémon.',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=standard_attack,
        ),
    ],
)

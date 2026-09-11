from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e4283786-17d8-596e-8c84-380eec375784',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sealeo.Name',
    display_name='Sealeo',
    searchable_by=['Sealeo', 'Stage 1', 'Sealeo'],
    subtypes=['Stage 1'],
    collector_number=25,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Spheal.Name',
    family_id=363,
    abilities=[
        Attack(
            title='Rest',
            game_text='Heal 60 damage from this Pokémon. This Pokémon is now Asleep.',
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Ice Ball',
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)

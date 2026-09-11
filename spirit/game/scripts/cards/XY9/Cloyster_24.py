from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='70af333e-9290-5d1a-b718-134a335faba8',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cloyster.Name',
    display_name='Cloyster',
    searchable_by=['Cloyster', 'Stage 1', 'Cloyster'],
    subtypes=['Stage 1'],
    collector_number=24,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Shellder.Name',
    family_id=90,
    abilities=[
        Attack(
            title='Sudden Grip',
            game_text="If this Pokémon evolved from Shellder during this turn, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=standard_attack,
        ),
        Attack(
            title='Surf',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)

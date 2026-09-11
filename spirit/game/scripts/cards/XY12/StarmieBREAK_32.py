from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5f919691-ad5d-5128-8541-83e036a17016',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.StarmieBREAK.Name',
    display_name='Starmie BREAK',
    searchable_by=['Starmie BREAK', 'BREAK', 'StarmieBREAK'],
    subtypes=['BREAK'],
    collector_number=32,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.BreakRare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Starmie.Name',
    family_id=120,
    abilities=[
        Attack(
            title='Break Star',
            game_text="This attack does 100 damage to each of your opponent's Pokémon BREAK. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bcd50a09-b009-59a5-ae2c-ed5a4072522b',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MachampBREAK.Name',
    display_name='Machamp BREAK',
    searchable_by=['Machamp BREAK', 'BREAK', 'MachampBREAK'],
    subtypes=['BREAK'],
    collector_number=60,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.BreakRare,
    hp=190,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Machamp.Name',
    family_id=66,
    abilities=[
        Attack(
            title='Boomerang Lariat',
            game_text="During your next turn, this Pokémon's attacks do 100 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 3},
            damage=100,
            effect=standard_attack,
        ),
    ],
)

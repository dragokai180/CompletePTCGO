from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='743a3746-c99a-583f-8c66-5ba0cb80ec23',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.ClawitzerBREAK.Name',
    display_name='Clawitzer BREAK',
    searchable_by=['Clawitzer BREAK', 'BREAK', 'ClawitzerBREAK'],
    subtypes=['BREAK'],
    collector_number=35,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.BreakRare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Clawitzer.Name',
    family_id=692,
    abilities=[
        Attack(
            title='Lock-On',
            game_text="The Defending Pokémon can't retreat during your opponent's next turn. During your next turn, any damage done to that Pokémon by attacks is increased by 120 (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)

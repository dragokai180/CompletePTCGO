from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8d0fe204-3170-5489-b132-47778a602f47',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dusknoir.Name',
    display_name='Dusknoir',
    searchable_by=['Dusknoir', 'Stage 2', 'Dusknoir'],
    subtypes=['Stage 2'],
    collector_number=85,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Dusclops.Name',
    family_id=355,
    abilities=[
        Ability(
            title='Grim Marking',
            game_text="If this Pokémon is your Active Pokémon and is Knocked Out by damage from an opponent's attack, put 4 damage counters on your opponent's Pokémon in any way you like.",
            passive=standard_passive("If this Pokémon is your Active Pokémon and is Knocked Out by damage from an opponent's attack, put 4 damage counters on your opponent's Pokémon in any way you like."),
        ),
        Attack(
            title='Psych Up',
            game_text="During your next turn, this Pokémon's Psych Up attack does 60 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=60,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5f519eec-9dad-5527-b10a-fd6bc4449c90',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gigalith.Name',
    display_name='Gigalith',
    searchable_by=['Gigalith', 'Stage 2', 'Gigalith'],
    subtypes=['Stage 2'],
    collector_number=50,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Boldore.Name',
    family_id=524,
    abilities=[
        Ability(
            title='High Density Armor',
            game_text="If this Pokémon has full HP, any damage done to this Pokémon by an opponent's attack is reduced by 50 (after applying Weakness and Resistance).",
            passive=standard_passive("If this Pokémon has full HP, any damage done to this Pokémon by an opponent's attack is reduced by 50 (after applying Weakness and Resistance)."),
        ),
        Attack(
            title='Overdrive Smash',
            game_text="During your next turn, this Pokémon's Overdrive Smash attack does 40 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

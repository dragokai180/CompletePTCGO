from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7f760b93-7cb6-52ea-8283-0dadcdcfbd8d',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Klinklang.Name',
    display_name='Klinklang',
    searchable_by=['Klinklang', 'Stage 2', 'Klinklang'],
    subtypes=['Stage 2'],
    collector_number=73,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Klang.Name',
    family_id=599,
    abilities=[
        Ability(
            title='Heavy Bumper',
            game_text="Any damage done to this Pokémon by an opponent's attack is reduced by 10 for each Colorless in your opponent's Active Pokémon's Retreat Cost (after applying Weakness and Resistance).",
            passive=standard_passive("Any damage done to this Pokémon by an opponent's attack is reduced by 10 for each Colorless in your opponent's Active Pokémon's Retreat Cost (after applying Weakness and Resistance)."),
        ),
        Attack(
            title='Gear Spinner',
            game_text="During your next turn, this Pokémon's Gear Spinner attack does 70 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=standard_attack,
        ),
    ],
)

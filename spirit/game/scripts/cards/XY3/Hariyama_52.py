from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8d06e0be-4251-5a0f-a7d0-271ee1eccb89',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hariyama.Name',
    display_name='Hariyama',
    searchable_by=['Hariyama', 'Stage 1', 'Hariyama'],
    subtypes=['Stage 1'],
    collector_number=52,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Makuhita.Name',
    family_id=296,
    abilities=[
        Ability(
            title='Thick Fat',
            game_text="Any damage done to this Pokémon by attacks from your opponent's Fire or Water Pokémon is reduced by 30 (after applying Weakness and Resistance).",
            passive=standard_passive("Any damage done to this Pokémon by attacks from your opponent's Fire or Water Pokémon is reduced by 30 (after applying Weakness and Resistance)."),
        ),
        Attack(
            title='Rocket Slap',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)

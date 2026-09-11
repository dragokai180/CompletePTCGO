from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ba7b8ffa-8af8-54f9-a135-3ec608b2590e',
    key='TATM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasSeviper.Name',
    display_name="Team Aqua's Seviper",
    searchable_by=["Team Aqua's Seviper", 'Basic', 'TeamAquasSeviper'],
    subtypes=['Basic'],
    collector_number=9,
    set_code='TATM',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=336,
    abilities=[
        Attack(
            title='Venomous Fang',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=standard_attack,
        ),
        Attack(
            title='Venom Tail',
            game_text="If your opponent's Active Pokémon is affected by a Special Condition, discard an Energy attached to that Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)

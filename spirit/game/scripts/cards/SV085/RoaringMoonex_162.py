from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="6599c675-fa54-531d-afbf-1d4585a72c9d",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RoaringMoonex.Name",
    display_name="Roaring Moon ex",
    searchable_by=["Roaring Moon ex", "Basic", "ex", "Ancient", "RoaringMoonex"],
    subtypes=["Basic", "ex", "Ancient"],
    collector_number=162,
    set_code="SV085",
    regulation_mark="G",
    rarity=Rarities.RareSecret,
    hp=230,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    abilities=[
        Attack(
            title="Frenzied Gouging",
            game_text="Knock Out your opponent's Active Pokémon. If your opponent's Active Pokémon is Knocked Out in this way, this Pokémon does 200 damage to itself.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title="Calamity Storm",
            game_text="You may discard a Stadium in play. If you do, this attack does 120 more damage.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)

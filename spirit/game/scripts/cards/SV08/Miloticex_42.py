from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="db5a1b52-319d-55cb-8b9d-139df20a3ec0",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Miloticex.Name",
    display_name="Milotic ex",
    searchable_by=["Milotic ex", "Stage 1", "ex", "Miloticex"],
    subtypes=["Stage 1", "ex"],
    collector_number=42,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Feebas.Name",
    family_id=349,
    abilities=[
        Ability(
            title="Sparkling Scales",
            game_text="Prevent all damage from and effects of attacks from your opponent's Tera Pokémon done to this Pokémon.",
            passive=standard_passive("Prevent all damage from and effects of attacks from your opponent's Tera Pokémon done to this Pokémon."),
        ),
        Attack(
            title="Hypno Splash",
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="7da46a72-fa1e-52a2-9897-54f00e28771c",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aerodactyl.Name",
    display_name="Aerodactyl",
    searchable_by=["Aerodactyl","RESTORED","Restored","Aerodactyl"],
    subtypes=["RESTORED","Restored"],
    collector_number=53,
    set_code="BW5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.OldAmberAerodactyl.Name",
    abilities=[
        Ability(
            title="Ancient Scream",
            game_text="Your Pokémon's attacks do 10 more damage to the Active Pokémon (before applying Weakness and Resistance).",
            passive=bw_legacy_passive("Your Pokémon's attacks do 10 more damage to the Active Pokémon (before applying Weakness and Resistance)."),
        ),
        Attack(
            title="Wing Attack",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
        ),
    ],
)

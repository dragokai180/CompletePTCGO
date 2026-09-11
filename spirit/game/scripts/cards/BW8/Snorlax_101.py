from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="9391f1fb-f06e-593c-a694-559cbcbe2734",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snorlax.Name",
    display_name="Snorlax",
    searchable_by=["Snorlax","Basic","Snorlax"],
    subtypes=["Basic"],
    collector_number=101,
    set_code="BW8",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    abilities=[
        Ability(
            title="Block",
            game_text="As long as this Pokémon is your Active Pokémon, your opponent's Active Pokémon can't retreat.",
            passive=bw_legacy_passive("As long as this Pokémon is your Active Pokémon, your opponent's Active Pokémon can't retreat."),
        ),
        Attack(
            title="Teampact",
            game_text="Does 30 damage times the number of Team Plasma Pokémon you have in play.",
            cost={PokemonTypes.COLORLESS: 5},
            damage=30,
            damage_operator="x",
            effect=bw_legacy_attack,
        ),
    ],
)

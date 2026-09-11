from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="525953ca-598a-5dfb-abee-966acf3dd4ea",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kecleon.Name",
    display_name="Kecleon",
    searchable_by=["Kecleon","Basic","Kecleon"],
    subtypes=["Basic"],
    collector_number=94,
    set_code="BW9",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    abilities=[
        Ability(
            title="Color Change",
            game_text="As long as this Pokémon is your Active Pokémon, this Pokémon is the same type as the your opponent's Active Pokémon.",
            passive=bw_legacy_passive("As long as this Pokémon is your Active Pokémon, this Pokémon is the same type as the your opponent's Active Pokémon."),
        ),
        Attack(
            title="Imittack",
            game_text="Choose 1 of the Defending Pokémon's attacks. If this Pokémon has the necessary Energy to use that attack, use it as this attack.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=bw_legacy_attack,
        ),
    ],
)

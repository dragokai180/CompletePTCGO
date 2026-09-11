from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="ee422255-ef19-5248-98b7-4d7d3eed04c9",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DeoxysEX.Name",
    display_name="Deoxys-EX",
    searchable_by=["Deoxys-EX","Basic","EX","DeoxysEX"],
    subtypes=["Basic","EX"],
    collector_number=53,
    set_code="BW9",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    abilities=[
        Ability(
            title="Power Connect",
            game_text="Your Team Plasma Pokémon's attacks (excluding Deoxys-EX) do 10 more damage to the Active Pokémon (before applying Weakness and Resistance).",
            passive=bw_legacy_passive("Your Team Plasma Pokémon's attacks (excluding Deoxys-EX) do 10 more damage to the Active Pokémon (before applying Weakness and Resistance)."),
        ),
        Attack(
            title="Helix Force",
            game_text="If this Pokémon has any Plasma Energy attached to it, this attack does 30 more damage for each Energy attached to the Defending Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
    ],
)

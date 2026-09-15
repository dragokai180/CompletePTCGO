from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import CursedGlarePassive, blizzard
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="4777e539-6f96-5cab-ab7d-9d4a72a90997",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ArticunoEX.Name",
    display_name="Articuno-EX",
    searchable_by=["Articuno-EX","Basic","EX","ArticunoEX","Team Plasma"],
    subtypes=["Basic","EX","Team Plasma"],
    collector_number=25,
    set_code="BW8",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    abilities=[
        Attack(
            title="Blizzard",
            game_text="Does 10 damage to each of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=blizzard,
        ),
        Attack(
            title="Frost Prison",
            game_text="If this Pokémon has any Plasma Energy attached to it, the Defending Pokémon is now Paralyzed.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=bw_legacy_attack,
        ),
    ],
)

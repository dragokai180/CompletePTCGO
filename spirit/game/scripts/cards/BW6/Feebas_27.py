from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="e8645082-32c9-5a44-94a5-14ca180db252",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Feebas.Name",
    display_name="Feebas",
    searchable_by=["Feebas","Basic","Feebas"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="BW6",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    abilities=[
        Attack(
            title="Add-a-Dash",
            game_text="Flip 2 coins. For each heads, draw a card.",
            cost={PokemonTypes.WATER: 1},
            effect=bw_legacy_attack,
        ),
    ],
)

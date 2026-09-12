from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="ead03687-f406-5e41-a15f-fddbed22ebef",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HeatranEX.Name",
    display_name="Heatran-EX",
    searchable_by=["Heatran-EX","Basic","EX","HeatranEX","Team Plasma"],
    subtypes=["Basic","EX","Team Plasma"],
    collector_number=109,
    set_code="BW9",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    abilities=[
        Attack(
            title="Heat Boiler",
            game_text="If this Pokémon is affected by a Special Condition, this attack does 60 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Dynamite Press",
            game_text="If this Pokémon has any Plasma Energy attached to it, this attack does 10 more damage for each damage counter on the Defending Pokémon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
    ],
)

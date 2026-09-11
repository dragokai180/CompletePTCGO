from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import deluge, deluge_condition, hydro_pump, powder_snow, reflect_energy
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="a0f42d04-6e6d-5d9f-b501-539dda73a2c8",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Watchog.Name",
    display_name="Watchog",
    searchable_by=["Watchog","Stage 1","Watchog"],
    subtypes=["Stage 1"],
    collector_number=119,
    set_code="BW7",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Patrat.Name",
    abilities=[
        Attack(
            title="Hypnoblast",
            game_text="The Defending Pokémon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=powder_snow,
        ),
        Attack(
            title="Psych Up",
            game_text="During your next turn, this Pokémon's Psych Up attack does 30 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=bw_legacy_attack,
        ),
    ],
)

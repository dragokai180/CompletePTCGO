from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="4d601c0b-78d8-522b-97dc-fa7dd852fe29",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Watchog.Name",
    display_name="Watchog",
    searchable_by=["Watchog","Stage 1","Watchog","Team Plasma"],
    subtypes=["Stage 1","Team Plasma"],
    collector_number=113,
    set_code="BW8",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Patrat.Name",
    abilities=[
        Attack(
            title="Second Bite",
            game_text="Does 10 more damage for each damage counter on the Defending Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Low Kick",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
    ],
)

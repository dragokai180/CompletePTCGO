from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import retribution, signal_beam
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="26b69657-8e44-5b71-8dbc-8f84b6a57079",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Starmie.Name",
    display_name="Starmie",
    searchable_by=["Starmie","Stage 1","Starmie"],
    subtypes=["Stage 1"],
    collector_number=24,
    set_code="BW4",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name",
    abilities=[
        Attack(
            title="Confuse Ray",
            game_text="The Defending Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=signal_beam,
        ),
        Attack(
            title="Swift",
            game_text="This attack's damage isn't affected by Weakness, Resistance, or any other effects on the Defending Pokémon.",
            cost={PokemonTypes.WATER: 1},
            damage=50,
            effect=bw_legacy_attack,
        ),
    ],
)

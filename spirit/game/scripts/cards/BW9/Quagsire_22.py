from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_ability, bw_legacy_attack, bw_legacy_passive, bw_stadium_ability, bw_stadium_triggers, bw_tool_abilities, bw_trainer_effect, bw_trainer_passive
from spirit.game.card_effects.bw10 import deluge, deluge_condition, hydro_pump, powder_snow, reflect_energy

card = PokemonCardDef(
    guid="6c70ddc1-425d-5d2c-addb-4d7b2f5e847c",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Quagsire.Name",
    display_name="Quagsire",
    searchable_by=["Quagsire","Stage 1","Quagsire"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="BW9",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wooper.Name",
    abilities=[
        Ability(
            title="Laid-Back",
            game_text="Any damage done to this Pokémon by attacks is reduced by 20 (after applying Weakness and Resistance).",
            passive=bw_legacy_passive("Any damage done to this Pokémon by attacks is reduced by 20 (after applying Weakness and Resistance)."),
        ),
        Attack(
            title="Mud Gun",
            game_text="If this Pokémon has any Fighting Energy attached to it, this attack does 30 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
    ],
)

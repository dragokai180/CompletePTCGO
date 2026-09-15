from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import switch_self_attack
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="f9452323-9b0d-5d74-8066-f31b27aa1d1a",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swanna.Name",
    display_name="Swanna",
    searchable_by=["Swanna","Stage 1","Swanna"],
    subtypes=["Stage 1"],
    collector_number=37,
    set_code="BW1",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ducklett.Name",
    abilities=[
        Attack(
            title="Feather Dance",
            game_text="During your next turn, each of this Pokémon's attacks does 40 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Aqua Ring",
            game_text="Switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=switch_self_attack(),
        ),
    ],
)

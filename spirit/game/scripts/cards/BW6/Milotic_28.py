from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import deluge, deluge_condition, hydro_pump, powder_snow, reflect_energy
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="ce64e555-aa4f-5dee-ba62-c9ab1d1f6cce",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Milotic.Name",
    display_name="Milotic",
    searchable_by=["Milotic","Stage 1","Milotic"],
    subtypes=["Stage 1"],
    collector_number=28,
    set_code="BW6",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Feebas.Name",
    abilities=[
        Attack(
            title="Clear Search",
            game_text="Search your deck for any 3 cards and put them into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.WATER: 1},
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Water Pulse",
            game_text="The Defending Pokémon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=powder_snow,
        ),
    ],
)

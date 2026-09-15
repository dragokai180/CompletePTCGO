from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import deluge, deluge_condition, hydro_pump, powder_snow, reflect_energy
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="ee458323-890a-5d58-90cf-0aae5a5e3dd0",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ivysaur.Name",
    display_name="Ivysaur",
    searchable_by=["Ivysaur","Stage 1","Ivysaur"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bulbasaur.Name",
    abilities=[
        Attack(
            title="Sleep Powder",
            game_text="The Defending Pokémon is now Asleep.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=powder_snow,
        ),
        Attack(
            title="Poison Powder",
            game_text="The Defending Pokémon is now Poisoned.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=bw_legacy_attack,
        ),
    ],
)

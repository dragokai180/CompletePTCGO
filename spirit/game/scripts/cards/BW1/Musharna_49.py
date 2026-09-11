from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import deluge, deluge_condition, hydro_pump, powder_snow, reflect_energy
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="cefb85ce-d300-55ca-b958-49e6c8bde804",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Musharna.Name",
    display_name="Musharna",
    searchable_by=["Musharna","Stage 1","Musharna"],
    subtypes=["Stage 1"],
    collector_number=49,
    set_code="BW1",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Munna.Name",
    abilities=[
        Attack(
            title="Hypnotic Ray",
            game_text="The Defending Pokémon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            effect=powder_snow,
        ),
        Attack(
            title="Dream Eater",
            game_text="If the Defending Pokémon is not Asleep, this attack does nothing.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=90,
            effect=bw_legacy_attack,
        ),
    ],
)

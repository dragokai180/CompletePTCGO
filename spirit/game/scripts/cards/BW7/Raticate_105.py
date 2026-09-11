from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="a592835b-5a78-57bd-b189-872307284e38",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raticate.Name",
    display_name="Raticate",
    searchable_by=["Raticate","Stage 1","Raticate"],
    subtypes=["Stage 1"],
    collector_number=105,
    set_code="BW7",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rattata.Name",
    abilities=[
        Attack(
            title="Gnaw Through",
            game_text="Discard a Pokémon Tool card attached to the Defending Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Super Fang",
            game_text="Put damage counters on the Defending Pokémon until its remaining HP is 10.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=bw_legacy_attack,
        ),
    ],
)

from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="1b06a4c5-f28a-5a0e-992b-552eb9154839",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golduck.Name",
    display_name="Golduck",
    searchable_by=["Golduck","Stage 1","Golduck"],
    subtypes=["Stage 1"],
    collector_number=35,
    set_code="BW7",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name",
    abilities=[
        Attack(
            title="Amnesia",
            game_text="Choose 1 of the Defending Pokémon's attacks. The Pokémon can't use that attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Aquafall",
            game_text="Discard all Energy attached to this Pokémon.",
            cost={PokemonTypes.WATER: 2},
            damage=90,
            effect=bw_legacy_attack,
        ),
    ],
)

from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="6516ec40-c7af-5248-8bd7-ab7f0fe47933",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Infernape.Name",
    display_name="Infernape",
    searchable_by=["Infernape","Stage 2","Infernape","Team Plasma"],
    subtypes=["Stage 2","Team Plasma"],
    collector_number=17,
    set_code="BW8",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Monferno.Name",
    abilities=[
        Attack(
            title="Torment",
            game_text="Choose 1 of the Defending Pokémon's attack. That Pokémon can't use that attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Malevolent Fire",
            game_text="Discard all Energy attached to this Pokémon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=bw_legacy_attack,
        ),
    ],
)

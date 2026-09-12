from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="6507bcdc-8b18-598e-a04b-746da849e045",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bisharp.Name",
    display_name="Bisharp",
    searchable_by=["Bisharp","Stage 1","Bisharp","Team Plasma"],
    subtypes=["Stage 1","Team Plasma"],
    collector_number=73,
    set_code="BW9",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pawniard.Name",
    abilities=[
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title="Dragon Slayer",
            game_text="If the Defending Pokémon is a Dragon Pokémon, this attack does 40 more damage.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
    ],
)

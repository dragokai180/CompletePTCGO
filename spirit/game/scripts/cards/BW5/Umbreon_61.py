from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import retribution, signal_beam
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="c912b95b-b2d0-5f2c-b635-c2738631de94",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Umbreon.Name",
    display_name="Umbreon",
    searchable_by=["Umbreon","Stage 1","Umbreon"],
    subtypes=["Stage 1"],
    collector_number=61,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    abilities=[
        Attack(
            title="Confuse Ray",
            game_text="The Defending Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=signal_beam,
        ),
        Attack(
            title="Shadow Shutdown",
            game_text="Flip 2 coins. If both of them are heads, discard all Energy attached to the Defending Pokémon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=bw_legacy_attack,
        ),
    ],
)

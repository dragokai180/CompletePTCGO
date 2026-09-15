from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="4f79cf32-4466-5cf1-9023-16e5bde404a2",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sigilyph.Name",
    display_name="Sigilyph",
    searchable_by=["Sigilyph","Basic","Sigilyph"],
    subtypes=["Basic"],
    collector_number=41,
    set_code="BW2",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    abilities=[
        Attack(
            title="Reflect",
            game_text="During your opponent's next turn, any damage done to this Pokémon by attacks is reduced by 40 (after applying Weakness and Resistance).",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Telekinesis",
            game_text="Does 50 damage to 1 of your opponent's Pokémon. This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            effect=bw_legacy_attack,
        ),
    ],
)

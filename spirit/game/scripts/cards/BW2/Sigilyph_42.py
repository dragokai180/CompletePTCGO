from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="70f9e204-0751-5411-995d-0ea30e6317d3",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sigilyph.Name",
    display_name="Sigilyph",
    searchable_by=["Sigilyph","Basic","Sigilyph"],
    subtypes=["Basic"],
    collector_number=42,
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
            title="Quick Turn",
            game_text="Flip 2 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=10),
        ),
        Attack(
            title="Psychic Assault",
            game_text="Does 10 more damage for each damage counter on the Defending Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
    ],
)

from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="0d414915-3e2f-5368-ae3b-c6b9826998fa",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Escavalier.Name",
    display_name="Escavalier",
    searchable_by=["Escavalier","Stage 1","Escavalier"],
    subtypes=["Stage 1"],
    collector_number=80,
    set_code="BW3",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Karrablast.Name",
    abilities=[
        Attack(
            title="Guard Press",
            game_text="During your opponent's next turn, any damage done to this Pokémon by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Twineedle",
            game_text="Flip 2 coins. This attack does 70 damage times the number of heads.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=70),
        ),
    ],
)

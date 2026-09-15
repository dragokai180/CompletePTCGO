from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import draw_until_effect
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="6661b9d3-b5b4-57bf-90b7-f6f549d11a5a",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lilligant.Name",
    display_name="Lilligant",
    searchable_by=["Lilligant","Stage 1","Lilligant"],
    subtypes=["Stage 1"],
    collector_number=17,
    set_code="BW7",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Petilil.Name",
    abilities=[
        Attack(
            title="Return",
            game_text="Draw cards until you have 6 cards in your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=draw_until_effect(6),
        ),
        Attack(
            title="Magical Leaf",
            game_text="Flip a coin. If heads, this attack does 30 more damage and heal 30 damage from this Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
    ],
)

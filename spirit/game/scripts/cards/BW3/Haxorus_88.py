from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import damage_per, flip_damage, lock_all_attacks
from spirit.game.card_effects.bw_era import bw_legacy_ability, bw_legacy_attack, bw_legacy_passive, bw_stadium_ability, bw_stadium_triggers, bw_tool_abilities, bw_trainer_effect, bw_trainer_passive
from spirit.game.session.legal_actions import energy_provided_count

async def giga_impact(ctx):
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)




card = PokemonCardDef(
    guid="b3e3e14a-c3e3-549c-ab4d-0cb26fdf37f1",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Haxorus.Name",
    display_name="Haxorus",
    searchable_by=["Haxorus","Stage 2","Haxorus"],
    subtypes=["Stage 2"],
    collector_number=88,
    set_code="BW3",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fraxure.Name",
    abilities=[
        Attack(
            title="Dual Chop",
            game_text="Flip 2 coins. This attack does 50 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=50),
        ),
        Attack(
            title="Giga Impact",
            game_text="This Pokémon can't attack during your next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=giga_impact,
        ),
    ],
)

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import damage_per, lock_all_attacks
from spirit.game.session.legal_actions import energy_provided_count
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

async def giga_impact(ctx):
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)



card = PokemonCardDef(
    guid="ccf58a40-604c-54c8-97ce-cd1b1e678faf",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stoutland.Name",
    display_name="Stoutland",
    searchable_by=["Stoutland","Stage 2","Stoutland"],
    subtypes=["Stage 2"],
    collector_number=83,
    set_code="BW1",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Herdier.Name",
    abilities=[
        Attack(
            title="Odor Sleuth",
            game_text="Flip 3 coins. For each heads, put a card from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Giga Impact",
            game_text="This Pokémon can't attack during your next turn.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=90,
            effect=giga_impact,
        ),
    ],
)

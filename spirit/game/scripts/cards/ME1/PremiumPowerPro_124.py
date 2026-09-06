from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.passives import TurnDamageModifier


async def premium_power_pro(ctx):
    """During this turn, attacks used by your Pokémon do 30 more damage to
    your opponent's Active Pokémon (before applying Weakness and Resistance)."""
    ctx.add_turn_damage_modifier(TurnDamageModifier(30, ctx.player_id))
    for pokemon in ctx.my_pokemon_in_play():
        await ctx.add_stat_visualization(
            pokemon, "Positive", "DamageDealtIncreased", card_text="+30 damage"
        )


card = ItemCardDef(
    guid="90acfdaa-e85a-5874-9490-b41356b07a25",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PremiumPowerPro.Name",
    display_name="Premium Power Pro",
    searchable_by=["Premium Power Pro","Item","PremiumPowerPro"],
    subtypes=["Item"],
    collector_number=124,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=premium_power_pro
)

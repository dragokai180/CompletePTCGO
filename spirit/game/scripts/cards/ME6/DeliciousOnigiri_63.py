from spirit.game.data_utils import ItemCardDef, def_for
from spirit.game.attributes import AttrID, Rarities
from spirit.game.session.passives import effective_max_hp


def _is_delicious_onigiri(card):
    return getattr(def_for(card.archetype_id), "display_name", None) == "Delicious Onigiri"


def _damaged_active(board, player_id, card=None):
    active = board.active_pokemon(player_id)
    if active is None:
        return False
    return active.get_attribute(AttrID.HP, 0) < effective_max_hp(board, active)


async def delicious_onigiri(ctx):
    """Heal 30 damage from your Active Pokemon. For each Delicious Onigiri card
    (not including this card) in your discard pile, heal 30 more damage from
    that Pokemon."""
    extras = sum(1 for c in ctx.discard_pile() if _is_delicious_onigiri(c))
    await ctx.heal(30 + 30 * extras, ctx.my_active())


card = ItemCardDef(
    guid="f6d359a5-fd5d-57b8-8cc7-89fcf75f8759",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DeliciousOnigiri.Name",
    display_name="Delicious Onigiri",
    searchable_by=["Delicious Onigiri","Item","DeliciousOnigiri"],
    subtypes=["Item"],
    collector_number=63,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Common,
    effect=delicious_onigiri,
    condition=_damaged_active,
)

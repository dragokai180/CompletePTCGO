from spirit.game.data_utils import SupporterCardDef, subtypes_for
from spirit.game.attributes import Rarities


def _prizes_remaining(board, player_id) -> int:
    area = board.find_player_area(player_id, "prizePile")
    return len(area.children) if area else 0


def _briar_condition(board, player_id) -> bool:
    opponent = next((p for p in board.player_ids if p != player_id), None)
    return opponent is not None and _prizes_remaining(board, opponent) == 2


async def briar(ctx):
    """This turn: +1 prize when opponent's Active is KO'd by damage from your
    Tera Pokémon's attack."""

    def _tera_attacker(attacker):
        return "Tera" in subtypes_for(attacker.archetype_id)

    def _opponent_active(target):
        return ctx.board.active_pokemon(target.owning_player_id) is target \
            and target.owning_player_id == ctx.opponent_id

    ctx.add_extra_prize_watcher(_tera_attacker, _opponent_active)


card = SupporterCardDef(
    guid="64256ecf-fbfd-5fc1-bb1c-4d2bd0d25916",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Briar.Name",
    display_name="Briar",
    searchable_by=["Briar", "Supporter", "Briar"],
    subtypes=["Supporter"],
    collector_number=132,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    condition=_briar_condition,
    effect=briar,
)

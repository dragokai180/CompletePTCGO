from spirit.game.data_utils import SupporterCardDef, has_rule_box
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import brandon_playable
from spirit.game.session.passives import Passive, carrier_pokemon


class _GladionsFinalBattlePassive(Passive):
    """Your Pokemon without a Rule Box do +80 to the opponent's Active."""

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        if calc.attacker is None:
            return
        if carrier_pokemon(carrier) is not calc.attacker:
            return
        if not has_rule_box(calc.attacker.archetype_id):
            calc.amount += 80


async def gladions_final_battle(ctx):
    for p in ctx.my_pokemon_in_play():
        ctx.add_temporary_passive(
            p,
            _GladionsFinalBattlePassive(),
            expires_after_turn=ctx.session.turn_state.turn_number,
        )


card = SupporterCardDef(
    guid="b76f8111-e02b-5252-9132-5cd88b96e248",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GladionsFinalBattle.Name",
    display_name="Gladion's Final Battle",
    searchable_by=["Gladion's Final Battle","Supporter","GladionsFinalBattle"],
    subtypes=["Supporter"],
    collector_number=77,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    effect=gladions_final_battle,
    condition=brandon_playable,
)

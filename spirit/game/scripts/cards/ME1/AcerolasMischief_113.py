from spirit.game.data_utils import SupporterCardDef, is_pokemon_ex
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive, carrier_pokemon


def _other_player(board, player_id):
    return next((p for p in board.player_ids if p != player_id), None)


def acerola_condition(board, player_id):
    opponent = _other_player(board, player_id)
    if not opponent:
        return False
    area = board.find_player_area(opponent, "prizePile")
    return bool(area) and len(area.children) <= 2


class AcerolaShieldPassive(Passive):
    """Prevent damage from and effects of opposing Pokemon ex attacks."""

    def prevents_damage(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return False
        if carrier_pokemon(carrier) is not calc.target:
            return False
        return calc.attacker is not None and is_pokemon_ex(calc.attacker.archetype_id)

    def blocks_attack_effects(self, target, carrier):
        return carrier_pokemon(carrier) is target


async def acerolas_mischief(ctx):
    """Choose 1 of your Pokémon. During your opponent's next turn, prevent
    all damage from and effects of attacks done to that Pokémon by your
    opponent's Pokémon ex."""
    target = await ctx.choose_pokemon(
        ctx.my_pokemon_in_play(), "Choose 1 of your Pokémon"
    )
    if target is None:
        return
    ctx.add_passive_through_opponents_turn(target, AcerolaShieldPassive())


card = SupporterCardDef(
    guid="834663f6-4afc-51e3-b405-d0f2c0a3702c",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AcerolasMischief.Name",
    display_name="Acerola's Mischief",
    searchable_by=["Acerola's Mischief","Supporter","AcerolasMischief"],
    subtypes=["Supporter"],
    collector_number=113,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=acerolas_mischief,
    condition=acerola_condition,
)

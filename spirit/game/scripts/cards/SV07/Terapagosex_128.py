from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import damage_per, count_bench
from spirit.game.card_effects.pokemon import TeraRulePassive
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.session.passives import Passive, carrier_pokemon


def _not_second_player_first_turn(board, player_id, pokemon=None) -> bool:
    """Unified Beatdown: if you go second, you can't use this on your first turn
    (global turn 2)."""
    ts = getattr(board, "turn_state", None)
    return ts is None or ts.turn_number != 2


class _CrownOpalShield(Passive):
    """Prevent damage from attacks by Basic non-Colorless Pokémon."""

    def prevents_damage(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing
                and carrier_pokemon(carrier) is calc.target):
            return False
        attacker = calc.attacker
        if attacker is None or not is_basic_pokemon(attacker):
            return False
        types = attacker.get_attribute(AttrID.POKEMON_TYPES) or []
        return PokemonTypes.COLORLESS.value not in types


async def crown_opal(ctx):
    """180. During opponent's next turn, prevent damage from Basic non-[C]."""
    await ctx.deal_damage()
    target = ctx.attacker
    if target is None:
        return
    ctx.add_passive_through_opponents_turn(target, _CrownOpalShield())


card = PokemonCardDef(
    guid="66208289-e577-582e-a7c6-6025b42fe4c8",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Terapagosex.Name",
    display_name="Terapagos ex",
    searchable_by=["Terapagos ex", "Basic", "ex", "Tera", "Terapagosex"],
    subtypes=["Basic", "ex", "Tera"],
    collector_number=128,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=230,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=1024,
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Unified Beatdown",
            game_text=(
                "If you go second, you can't use this attack during your first "
                "turn. This attack does 30 damage for each of your Benched Pokémon."
            ),
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            condition=_not_second_player_first_turn,
            effect=damage_per(count_bench("mine"), 30),
        ),
        Attack(
            title="Crown Opal",
            game_text=(
                "During your opponent's next turn, prevent all damage done to "
                "this Pokémon by attacks from Basic non-[C] Pokémon."
            ),
            cost={
                PokemonTypes.GRASS: 1,
                PokemonTypes.WATER: 1,
                PokemonTypes.LIGHTNING: 1,
            },
            damage=180,
            effect=crown_opal,
        ),
    ],
)

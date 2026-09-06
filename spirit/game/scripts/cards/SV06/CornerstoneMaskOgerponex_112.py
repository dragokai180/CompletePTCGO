from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.pokemon import TeraRulePassive
from spirit.game.session.passives import Passive


class _CornerstoneStancePassive(Passive):
    """Prevent damage from attacks by opponent Pokémon that have an Ability."""

    def prevents_damage(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.target is carrier):
            return False
        attacker = calc.attacker
        if attacker is None:
            return False
        return any(
            isinstance(entry, dict) and entry.get("abilityType") != "Attack"
            for entry in (attacker.get_attribute(AttrID.PIE_ABILITIES) or [])
        )


async def demolish(ctx):
    """140. Ignore Weakness/Resistance and opponent Active effects."""
    await ctx.deal_damage(
        ignore_weakness=True,
        ignore_resistance=True,
        ignore_target_effects=True,
    )


card = PokemonCardDef(
    guid="68ca4dc3-b6a3-46db-a4bb-2aa582e31aae",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CornerstoneMaskOgerponex.Name",
    display_name="Cornerstone Mask Ogerpon ex",
    searchable_by=[
        "Cornerstone Mask Ogerpon ex",
        "Basic",
        "ex",
        "Tera",
        "CornerstoneMaskOgerponex",
    ],
    subtypes=["Basic", "ex", "Tera"],
    collector_number=112,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=210,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=1017,
    passive=TeraRulePassive(),
    abilities=[
        Ability(
            title="Cornerstone Stance",
            game_text=(
                "Prevent all damage from attacks done to this Pokémon by your "
                "opponent's Pokémon that have an Ability."
            ),
            passive=_CornerstoneStancePassive(),
        ),
        Attack(
            title="Demolish",
            game_text=(
                "This attack's damage isn't affected by Weakness or Resistance, "
                "or by any effects on your opponent's Active Pokémon."
            ),
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=140,
            effect=demolish,
        ),
    ],
)


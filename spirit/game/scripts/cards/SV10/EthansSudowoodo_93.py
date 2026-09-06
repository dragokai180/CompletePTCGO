from spirit.game.data_utils import PokemonCardDef, Attack, def_for
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities


async def impound(ctx):
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None and not ctx.effects_blocked(defender):
        ctx.lock_retreat(defender)


async def try_to_imitate(ctx):
    """Flip a coin. If heads, copy 1 of the opponent's Active attacks."""
    heads = (await ctx.flip_coins(1, "Try to Imitate"))[0]
    if not heads:
        return
    defender = ctx.opponent_active()
    if defender is None:
        return
    definition = def_for(defender.archetype_id)
    candidates = [
        (defender, ability) for ability in getattr(definition, "abilities", [])
        if isinstance(ability, Attack)
    ]
    if not candidates:
        return
    picked = await ctx.choose_attack_to_copy(candidates, "Choose an attack to copy")
    if picked is None:
        return
    _, chosen = picked
    if not await ctx.use_attack(chosen):
        return
    if getattr(chosen, "locks_next_turn", False):
        for entry in ctx.attacker.get_attribute(AttrID.PIE_ABILITIES) or []:
            if isinstance(entry, dict) and entry.get("abilityType") == "Attack":
                ctx.session.turn_state.lock_attack(
                    ctx.attacker.entity_id, entry["abilityID"]
                )


card = PokemonCardDef(
    guid="abce8386-f187-5935-91ba-c1993548c5f5",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EthansSudowoodo.Name",
    display_name="Ethan's Sudowoodo",
    searchable_by=["Ethan's Sudowoodo", "Basic", "EthansSudowoodo"],
    subtypes=["Basic"],
    collector_number=93,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=185,
    abilities=[
        Attack(
            title="Impound",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=impound,
        ),
        Attack(
            title="Try to Imitate",
            game_text="Flip a coin. If heads, choose 1 of your opponent's Active Pokémon's attacks and use it as this attack.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=try_to_imitate,
        ),
    ],
)

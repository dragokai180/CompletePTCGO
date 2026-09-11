from spirit.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import retribution, signal_beam

async def assist(ctx):
    """Flip a coin. If heads, choose 1 of your Benched Pokémon's attacks and
    use it as this attack."""
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
    guid="706f6a5e-33c1-5912-85d8-044837a7cf1e",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Liepard.Name",
    display_name="Liepard",
    searchable_by=["Liepard","Stage 1","Liepard"],
    subtypes=["Stage 1"],
    collector_number=91,
    set_code="BW7",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Purrloin.Name",
    abilities=[
        Attack(
            title="Tail Trickery",
            game_text="The Defending Pokémon is now Confused.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=signal_beam,
        ),
        Attack(
            title="Assist",
            game_text="Flip a coin. If heads, choose 1 of your Benched Pokémon's attacks and use it as this attack.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            effect=assist,
        ),
    ],
)

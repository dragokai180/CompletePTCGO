from spirit.game.data_utils import PokemonCardDef, Attack, def_for, subtypes_for
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities


async def gemstone_mimicry(ctx):
    """Choose 1 of your opponent's Active Tera Pokémon's attacks and use it."""
    defender = ctx.opponent_active()
    if defender is None or "Tera" not in subtypes_for(defender.archetype_id):
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


def _gemstone_condition(board, player_id, pokemon=None) -> bool:
    opponent = next((p for p in board.player_ids if p != player_id), None)
    if opponent is None:
        return False
    target = board.active_pokemon(opponent)
    return target is not None and "Tera" in subtypes_for(target.archetype_id)


card = PokemonCardDef(
    guid="c8130f00-efbf-5281-87b0-b0e550466b00",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsMimikyu.Name",
    display_name="Team Rocket's Mimikyu",
    searchable_by=["Team Rocket's Mimikyu", "Basic", "TeamRocketsMimikyu"],
    subtypes=["Basic"],
    collector_number=87,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=778,
    abilities=[
        Attack(
            title="Gemstone Mimicry",
            game_text="Choose 1 of your opponent's Active Tera Pokémon's attacks and use it as this attack.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            condition=_gemstone_condition,
            effect=gemstone_mimicry,
        ),
    ],
)

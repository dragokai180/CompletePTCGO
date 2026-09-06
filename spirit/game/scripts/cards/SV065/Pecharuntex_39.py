from spirit.game.data_utils import PokemonCardDef, Ability, Attack, Activations
from spirit.game.attributes import (
    PokemonTypes,
    PokemonStage,
    Rarities,
    AttrID,
    SpecialConditions,
)
from spirit.game.card_effects.attacks_common import count_prizes_taken

PECHARUNT_EX_GUID = "d9ce4ae0-25bc-476d-9be7-d1d7459d1bbe"


def _subjugating_chains_condition(board, player_id, pokemon) -> bool:
    # Need at least 1 eligible benched [D] Pokémon (excluding Pecharunt ex).
    bench = board.find_player_area(player_id, "bench")
    if not bench:
        return False
    for c in bench.children:
        if c.archetype_id == PECHARUNT_EX_GUID:
            continue
        types = c.get_attribute(AttrID.POKEMON_TYPES) or []
        if PokemonTypes.DARKNESS.value in types:
            return True
    return False


async def subjugating_chains(ctx):
    candidates = []
    for p in ctx.my_bench():
        if p.archetype_id == PECHARUNT_EX_GUID:
            continue
        types = p.get_attribute(AttrID.POKEMON_TYPES) or []
        if PokemonTypes.DARKNESS.value in types:
            candidates.append(p)

    if not candidates:
        return

    target = await ctx.choose_pokemon(candidates, "Choose a Benched Darkness Pokémon")
    if target is None:
        return

    await ctx.switch_active(ctx.player_id, target)
    # The new Active Pokémon is now Poisoned.
    await ctx.apply_special_condition(ctx.my_active(), SpecialConditions.POISONED)

async def irritated_outburst(ctx):
    amount = 60 * count_prizes_taken("opponent")(ctx)
    if amount <= 0:
        return
    await ctx.deal_damage(amount)


card = PokemonCardDef(
    guid=PECHARUNT_EX_GUID,
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pecharuntex.Name",
    display_name="Pecharunt ex",
    searchable_by=["Pecharunt ex", "Basic", "ex", "Pecharuntex"],
    subtypes=["Basic", "ex"],
    collector_number=39,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=190,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=1025,
    abilities=[
        Ability(
            title="Subjugating Chains",
            game_text=(
                "Once during your turn, you may switch 1 of your Benched "
                "[D] Pokémon, except any Pecharunt ex, with your Active "
                "Pokémon. If you do, the new Active Pokémon is now Poisoned.\n\n"
                "You can't use more than 1 Subjugating Chains Ability each turn."
            ),
            activation=Activations.ONCE_PER_TURN,
            shared_once_per_turn="Subjugating Chains",
            condition=_subjugating_chains_condition,
            effect=subjugating_chains,
        ),
        Attack(
            title="Irritated Outburst",
            game_text="",
            cost={PokemonTypes.DARKNESS: 2},
            damage=60,
            damage_operator="x",
            effect=irritated_outburst,
        ),
    ],
)


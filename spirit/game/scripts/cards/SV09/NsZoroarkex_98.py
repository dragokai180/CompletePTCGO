from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.support_common import discard_then_draw, requires_hand
from spirit.game.models.board import PokemonEntity


def _is_ns_pokemon(pokemon) -> bool:
    definition = def_for(pokemon.archetype_id)
    name = getattr(definition, "display_name", "") or ""
    return name.startswith("N's ")


def _ns_bench_attacks(ctx):
    pairs = []
    seen = set()
    for pokemon in ctx.my_bench():
        if not isinstance(pokemon, PokemonEntity) or not _is_ns_pokemon(pokemon):
            continue
        definition = def_for(pokemon.archetype_id)
        for ability in getattr(definition, "abilities", []):
            if isinstance(ability, Attack):
                key = (ability.title, ability.game_text)
                if key in seen:
                    continue
                seen.add(key)
                pairs.append((pokemon, ability))
    return pairs


async def night_joker(ctx):
    """Choose 1 of your Benched N's Pokémon's attacks and use it as this attack."""
    candidates = _ns_bench_attacks(ctx)
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
    guid="c5c014eb-f24a-56c0-8123-d6f03e1650ec",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NsZoroarkex.Name",
    display_name="N's Zoroark ex",
    searchable_by=["N's Zoroark ex", "Stage 1", "ex", "NsZoroarkex"],
    subtypes=["Stage 1", "ex"],
    collector_number=98,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=280,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.NsZorua.Name",
    family_id=570,
    abilities=[
        Ability(
            title="Trade",
            game_text="You must discard a card from your hand in order to use this Ability. Once during your turn, you may draw 2 cards.",
            activation=Activations.ONCE_PER_TURN,
            condition=requires_hand(n=1),
            effect=discard_then_draw(1, 2, optional=False),
        ),
        Attack(
            title="Night Joker",
            game_text="Choose 1 of your Benched N's Pokémon's attacks and use it as this attack.",
            cost={PokemonTypes.DARKNESS: 2},
            effect=night_joker,
        ),
    ],
)

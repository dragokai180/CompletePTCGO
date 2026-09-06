from spirit.game.data_utils import PokemonCardDef, Attack, def_for, has_rule_box
from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.session.effects import is_pokemon_card


async def seek_inspiration(ctx):
    """Discard the top card of your deck; if it's a Pokémon without a Rule
    Box, copy one of its attacks."""
    top = ctx.deck_top(1)
    if not top:
        return
    await ctx.discard_cards(top)
    card = top[0]
    if not is_pokemon_card(card) or has_rule_box(card.archetype_id):
        return
    definition = def_for(card.archetype_id)
    candidates = [
        (card, ability) for ability in getattr(definition, "abilities", [])
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
    guid="204edd67-b561-5e10-a1e7-3102b0a9d477",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowking.Name",
    display_name="Slowking",
    searchable_by=["Slowking","Stage 1","Slowking"],
    subtypes=["Stage 1"],
    collector_number=58,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    family_id=79,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    abilities=[
        Attack(
            title="Seek Inspiration",
            game_text="Discard the top card of your deck, and if that card is a Pokémon that doesn't have a Rule Box, choose 1 of its attacks and use it as this attack. (Pokémon ex, Pokémon V, etc. have Rule Boxes.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=seek_inspiration,
        ),
        Attack(
            title="Super Psy Bolt",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)

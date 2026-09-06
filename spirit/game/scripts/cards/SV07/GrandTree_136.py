from spirit.game.data_utils import StadiumCardDef, Ability, Activations
from spirit.game.attributes import AttrID, PokemonStage, Rarities
from spirit.game.session.effects import is_basic_pokemon, is_pokemon_card


def _is_stage1(card) -> bool:
    return is_pokemon_card(card) \
        and card.get_attribute(AttrID.STAGE) == PokemonStage.STAGE1.value


def _is_stage2(card) -> bool:
    return is_pokemon_card(card) \
        and card.get_attribute(AttrID.STAGE) == PokemonStage.STAGE2.value


def _grand_tree_condition(board, player_id, stadium=None) -> bool:
    turn_state = getattr(board, "turn_state", None)
    if turn_state is None:
        return False
    return any(
        is_basic_pokemon(p) and turn_state.may_evolve_target(p.entity_id)
        for p in board.pokemon_in_play(player_id)
    )


async def grand_tree(ctx):
    """Search for a Stage 1 that evolves from one of your eligible Basics and
    evolve it; if you did, you may then evolve that into a Stage 2 from deck."""
    turn_state = ctx.session.turn_state
    candidates = [
        p for p in ctx.my_pokemon_in_play()
        if is_basic_pokemon(p) and turn_state.may_evolve_target(p.entity_id)
    ]
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose a Basic Pokémon to evolve"
    )
    if target is None:
        return
    logic_name = target.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
    if not logic_name:
        return

    stage1_picks = await ctx.search_deck(
        lambda c, name=logic_name: (
            _is_stage1(c)
            and c.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == name
        ),
        count=1, minimum=0,
        prompt="Choose a Stage 1 Pokémon that evolves from that Pokémon.",
    )
    if not stage1_picks:
        await ctx.shuffle_deck()
        return
    await ctx.evolve_pokemon(target, stage1_picks[0])
    stage1 = stage1_picks[0]
    stage1_logic = stage1.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
    if not stage1_logic:
        await ctx.shuffle_deck()
        return

    if not await ctx.ask_yes_no(
        "Search your deck for a Stage 2 Pokémon that evolves from that Pokémon?"
    ):
        await ctx.shuffle_deck()
        return

    stage2_picks = await ctx.search_deck(
        lambda c, name=stage1_logic: (
            _is_stage2(c)
            and c.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == name
        ),
        count=1, minimum=0,
        prompt="Choose a Stage 2 Pokémon that evolves from that Pokémon.",
    )
    if stage2_picks:
        await ctx.evolve_pokemon(stage1, stage2_picks[0])
    await ctx.shuffle_deck()


GRAND_TREE_ABILITY = Ability(
    title="Grand Tree",
    game_text=(
        "Once during each player's turn, that player may search their deck for "
        "a Stage 1 Pokémon that evolves from 1 of their Basic Pokémon and put "
        "it onto that Pokémon to evolve it. If that Pokémon was evolved in this "
        "way, that player may search their deck for a Stage 2 Pokémon that "
        "evolves from that Pokémon and put it onto that Pokémon to evolve it. "
        "Then, that player shuffles their deck. (Players can't evolve a Basic "
        "Pokémon during their first turn or a Basic Pokémon that was put into "
        "play this turn.)"
    ),
    activation=Activations.ONCE_PER_TURN,
    effect=grand_tree,
    condition=_grand_tree_condition,
)


card = StadiumCardDef(
    guid="52fab9fe-ae3d-5752-bcee-193a656c9295",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GrandTree.Name",
    display_name="Grand Tree",
    searchable_by=["Grand Tree", "Stadium", "ACE SPEC", "GrandTree"],
    subtypes=["Stadium", "ACE SPEC"],
    collector_number=136,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.RareUltra,
    ability=GRAND_TREE_ABILITY,
)

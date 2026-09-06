from spirit.game.data_utils import PokemonCardDef, Ability, Attack, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.constants import BENCH_CAPACITY


DUSKULL_GUID = "eb9fd2e6-7cf4-4523-a899-61f45834ac12"


def _come_and_get_you_condition(board, player_id, pokemon) -> bool:
    bench = board.find_player_area(player_id, "bench")
    if not bench or len(bench.children) >= BENCH_CAPACITY:
        return False
    discard = board.find_player_area(player_id, "discard")
    if not discard:
        return False
    return any(
        c.archetype_id == DUSKULL_GUID
        for c in discard.children
        if getattr(c, "archetype_id", None)
    )


async def come_and_get_you(ctx):
    """Put up to 3 Duskull from your discard pile onto your Bench."""
    candidates = [c for c in ctx.discard_pile() if c.archetype_id == DUSKULL_GUID]
    if not candidates:
        return
    space = BENCH_CAPACITY - len(ctx.my_bench())
    if space <= 0:
        return
    count = min(3, space)
    picks = await ctx.choose_cards(
        candidates,
        count,
        minimum=0,
        prompt="Choose up to 3 Duskull to put onto your Bench.",
    )
    for card in picks:
        await ctx.bench_pokemon(card)


card = PokemonCardDef(
    guid=DUSKULL_GUID,
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Duskull.Name",
    display_name="Duskull",
    searchable_by=["Duskull", "Basic", "Duskull"],
    subtypes=["Basic"],
    collector_number=18,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=355,
    abilities=[
        Ability(
            title="Come and Get You",
            game_text="Put up to 3 Duskull from your discard pile onto your Bench.",
            activation=Activations.ONCE_PER_TURN,
            condition=_come_and_get_you_condition,
            effect=come_and_get_you,
        ),
        Attack(
            title="Mumble",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=30,
        ),
    ],
)


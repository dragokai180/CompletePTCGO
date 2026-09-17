from spirit.game.data_utils import PokemonCardDef, Attack, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import effective_bench_capacity


DUSKULL_GUID = "eb9fd2e6-7cf4-4523-a899-61f45834ac12"


async def come_and_get_you(ctx):
    """Put up to 3 Duskull from your discard pile onto your Bench."""
    candidates = [c for c in ctx.discard_pile()
                  if getattr(def_for(c.archetype_id), "display_name", None) == "Duskull"]
    if not candidates:
        return
    space = effective_bench_capacity(ctx.board, ctx.player_id) - len(ctx.my_bench())
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
        Attack(
            title="Come and Get You",
            game_text="Put up to 3 Duskull from your discard pile onto your Bench.",
            cost={PokemonTypes.PSYCHIC: 1},
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


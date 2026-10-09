from spirit.game.data_utils import SupporterCardDef, def_for
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_pokemon_card
from spirit.game.session.passives import effective_bench_capacity


_RESTORED_NAMES = {"Amaura", "Tyrunt"}


def fossil_researcher_condition(board, player_id):
    deck = board.find_player_area(player_id, "deck")
    bench = board.find_player_area(player_id, "bench")
    return bool(deck is not None and deck.children and bench is not None
                and len(bench.children) < effective_bench_capacity(board, player_id))


async def fossil_researcher(ctx):
    free = max(0, effective_bench_capacity(ctx.board, ctx.player_id)
               - len(ctx.my_bench()))
    count = min(2, free)
    if count:
        picks = await ctx.search_deck(
            lambda card: is_pokemon_card(card) and
            getattr(def_for(card.archetype_id), "display_name", "") in _RESTORED_NAMES,
            count=count, minimum=0,
            prompt="Choose up to 2 Amaura or Tyrunt",
        )
        for card in picks:
            await ctx.bench_pokemon(card)
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid='2be42883-d054-599b-a803-32ff6d6faba9',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.FossilResearcher.Name',
    display_name='Fossil Researcher',
    searchable_by=['Fossil Researcher', 'Supporter', 'FossilResearcher'],
    subtypes=['Supporter'],
    collector_number=92,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=fossil_researcher,
    condition=fossil_researcher_condition,
)

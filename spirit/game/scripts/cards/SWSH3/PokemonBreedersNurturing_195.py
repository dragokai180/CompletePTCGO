from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import AttrID, Rarities
from spirit.game.card_effects.trainer_followup import evosoda_condition, evosoda_targets


def _breeders_nurturing_condition(board, player_id):
    return evosoda_condition(board, player_id)


async def pokemon_breeders_nurturing(ctx):
    """Choose up to 2 of your Pokemon in play (not put into play this turn);
    for each, search the deck for a card that evolves from it and evolve it."""
    if not evosoda_condition(ctx.board, ctx.player_id):
        return
    candidates = evosoda_targets(ctx.board, ctx.player_id)
    if not candidates:
        return
    targets = await ctx.choose_cards(
        candidates, min(2, len(candidates)), minimum=0,
        prompt="Choose up to 2 of your Pokémon in play to evolve.",
    )
    if not targets:
        return
    for target in targets:
        logic_name = target.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
        if not logic_name:
            continue
        picks = await ctx.search_deck(
            lambda c, name=logic_name: c.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == name,
            count=1, minimum=0,
            prompt="Choose a card that evolves from that Pokémon.",
        )
        if picks:
            await ctx.evolve_pokemon(target, picks[0])
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid="f208756d-1c45-50e1-8fe0-61a971d8fd8e",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonBreedersNurturing.Name",
    display_name="Pokémon Breeder's Nurturing",
    searchable_by=["Pokémon Breeder's Nurturing", "Supporter"],
    subtypes=["Supporter"],
    collector_number=195,
    set_code="SWSH3",
    rarity=Rarities.RareRainbow,
    effect=pokemon_breeders_nurturing,
    condition=_breeders_nurturing_condition
)

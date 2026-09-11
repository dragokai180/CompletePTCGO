from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_ability, bw_legacy_attack, bw_legacy_passive, bw_stadium_ability, bw_stadium_triggers, bw_tool_abilities, bw_trainer_effect, bw_trainer_passive

async def future_sight(ctx):
    """Look at the top 5 cards of your deck and put them back on top of your
    deck in any order."""
    top = ctx.deck_top(5, ctx.opponent_id)
    if len(top) <= 1:
        return
    picked_ids = await ctx.session.prompt_card_chooser(
        ctx.player_id, ctx.source.entity_id, top, len(top), minimum=len(top),
        prompt="Put the cards back in any order.", ordered=True,
    )
    by_id = {c.entity_id: c for c in top}
    order = [by_id[i] for i in picked_ids if i in by_id]
    for card in top:
        if card not in order:
            order.append(card)
    deck = ctx.board.find_player_area(ctx.opponent_id, "deck")
    for card in order:
        deck.children.remove(card)
    for card in reversed(order):
        deck.children.append(card)



card = PokemonCardDef(
    guid="2430e7dc-c043-5c2e-817c-b71ee2a23c0f",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gothita.Name",
    display_name="Gothita",
    searchable_by=["Gothita","Basic","Gothita"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="BW6",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    abilities=[
        Attack(
            title="Future Sight",
            game_text="Look at the top 5 cards of your deck and put them back on top of your deck in any order.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=future_sight,
        ),
    ],
)

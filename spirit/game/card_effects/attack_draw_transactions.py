"""Compound draw instructions that must not fall through to a second clause."""
import re

from spirit.game.attributes import PokemonTypes
from spirit.game.session.effects import is_pokemon_card
from spirit.game.session.passives import Passive, effective_retreat_cost


class _SkipTurnDraw(Passive):
    def __init__(self, player_id):
        self.player_id = player_id

    def blocks_turn_draw(self, player_id, carrier):
        return player_id == self.player_id


async def resolve_draw_transaction(ctx, text, printed):
    from spirit.game.card_effects.bw_era import _name, _energy_count, _is_type

    # Do not interpret "can't draw" as an instruction to draw for the attacker.
    if re.fullmatch(
        r"flip a coin\. if heads, your opponent can't draw a card at the "
        r"beginning of (?:his or her|their) next turn\.", text
    ):
        if printed:
            await ctx.deal_damage(printed)
        if (await ctx.flip_coins(1, ctx.ability.title))[0]:
            ctx.add_temporary_player_passive(
                ctx.opponent_id, _SkipTurnDraw(ctx.opponent_id),
                ctx.session.turn_state.turn_number + 1)
        return True

    top_choice = re.fullmatch(
        r"look at the top (?:(\d+) cards|card) of your deck\. "
        r"you may put (?:it|that card|those cards) into your hand\. "
        r"if (?:not|you don't), discard (?:it|that card|those cards) and "
        r"draw (a|\d+) cards?\.", text)
    if top_choice:
        if printed:
            await ctx.deal_damage(printed)
        cards = ctx.deck_top(int(top_choice[1] or 1))
        if cards:
            await ctx.reveal_cards(cards, to_player=ctx.player_id)
            if await ctx.ask_yes_no("Put these cards into your hand?"):
                await ctx.put_in_hand(cards, reveal=False)
            else:
                await ctx.discard_cards(cards)
                await ctx.draw_cards(1 if top_choice[2] == 'a' else int(top_choice[2]))
        return True

    lost_payment = re.fullmatch(
        r"(?:choose a card from your hand and put it|put a card from your hand) "
        r"in the lost zone\. (?:if you do,|then,) draw (\d+) cards\.", text)
    if lost_payment:
        if printed:
            await ctx.deal_damage(printed)
        hand = list(ctx.hand())
        chosen = await ctx.choose_cards(hand, 1, minimum=1,
            prompt="Choose a card to put in the Lost Zone") if hand else []
        if chosen:
            await ctx.move_to_lost_zone(chosen)
            await ctx.draw_cards(int(lost_payment[1]))
        return True

    bottom_draw = re.fullmatch(r"draw (\d+) cards from the bottom of your deck\.", text)
    if bottom_draw:
        if printed:
            await ctx.deal_damage(printed)
        await ctx.draw_cards(int(bottom_draw[1]), from_bottom=True)
        return True

    board_draw = re.fullmatch(r"draw a card for each (.+)\.", text)
    if board_draw:
        descriptor = board_draw[1]
        count = None
        energy = re.fullmatch(r"(\w+) energy attached to all of your pokémon", descriptor)
        retreat = re.fullmatch(r"of your pokémon in play that has a retreat cost of exactly (\d+)", descriptor)
        named = re.fullmatch(r"of your (.+) in play", descriptor)
        if energy:
            count = sum(_energy_count(ctx, p, energy[1]) for p in ctx.my_pokemon_in_play())
        elif retreat:
            count = sum(effective_retreat_cost(ctx.board, p) == int(retreat[1])
                        for p in ctx.my_pokemon_in_play())
        elif named:
            noun = named[1]
            kind = getattr(PokemonTypes, noun.removesuffix(' pokémon').upper(), None)
            count = sum(
                noun == 'pokémon' or (_is_type(p, kind) if kind else _name(p).casefold() == noun)
                for p in ctx.my_pokemon_in_play())
        if count is not None:
            if printed:
                await ctx.deal_damage(printed)
            await ctx.draw_cards(count)
            return True

    if text.startswith("put a pokémon from your hand face down in front of you."):
        if printed:
            await ctx.deal_damage(printed)
        pool = [c for c in ctx.hand() if is_pokemon_card(c)]
        picks = await ctx.choose_cards(pool, 1, minimum=1,
            prompt="Choose a Pokémon") if pool else []
        if picks:
            names = ["Grass", "Fire", "Water", "Lightning", "Psychic", "Fighting",
                     "Darkness", "Metal", "Fairy", "Dragon", "Colorless"]
            guess = await ctx.choose("Guess that Pokémon's type", names,
                                     player_id=ctx.opponent_id)
            await ctx.reveal_cards(picks)
            from spirit.game.attributes import AttrID
            correct = getattr(PokemonTypes, names[guess].upper()).value in (
                picks[0].get_attribute(AttrID.POKEMON_TYPES) or [])
            await ctx.draw_cards(4, player_id=ctx.opponent_id if correct else ctx.player_id)
        return True
    return False

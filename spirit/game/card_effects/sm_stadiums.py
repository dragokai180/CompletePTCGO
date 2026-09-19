"""Ordered SM Stadium actions written in the acting player's third person.

The generic Pokemon Ability interpreter expects 'your deck/hand'. Stadium
rules instead say 'that player/their deck', so resolve these explicit
families before falling back to that interpreter. Reprints share the text.
"""
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.data_utils import subtypes_for, has_rule_box
from spirit.game.session.effects import is_basic_energy, is_basic_pokemon, is_pokemon_tool, is_pokemon_card
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.session.passives import effective_bench_capacity


def stadium_effect_for_text(text):
    t = ' '.join(text.casefold().split())
    discard_search = 'that player may discard a card from their hand' in t and 'searches their deck for' in t
    heat_factory = 'that player may discard a fire energy card from their hand' in t and 'draw 3 cards' in t
    coronet = 'that player may put 2 metal energy cards from their discard pile into their hand' in t
    brooklet = 'search their deck for a basic water pokémon or basic fighting pokémon' in t
    ultra_space = 'search their deck for an ultra beast card' in t
    artazon = "search their deck for a basic pokémon that doesn't have a rule box" in t
    lumiose = 'search their deck for a basic pokémon and put it onto their bench' in t
    town_store = 'search their deck for a pokémon tool card' in t
    mesagoza = 'flip a coin' in t and 'searches their deck for a pokémon' in t
    if not any((discard_search, heat_factory, coronet, brooklet, ultra_space,
                artazon, lumiose, town_store, mesagoza)):
        return None

    async def effect(ctx):
        if coronet:
            eligible = [c for c in ctx.discard_pile() if energy_provides_type(c, PokemonTypes.METAL.value)]
            if eligible:
                count = min(2, len(eligible))
                picks = await ctx.choose_cards(eligible, count, minimum=count, prompt='Choose Metal Energy cards')
                await ctx.put_in_hand(picks, reveal=True)
            return
        if not ctx.deck():
            return
        if artazon or lumiose:
            if len(ctx.my_bench()) >= effective_bench_capacity(ctx.board, ctx.player_id):
                return
            cards = await ctx.search_deck(
                lambda c: is_basic_pokemon(c) and ctx.can_bench_pokemon(c)
                and (not artazon or not has_rule_box(c.archetype_id)),
                count=1, minimum=0, prompt='Choose a Basic Pokémon for your Bench')
            for card in cards:
                await ctx.bench_pokemon(card)
            await ctx.shuffle_deck()
            # Failing a private search still ends the turn with Lumiose City.
            if lumiose and 'their turn ends' in t:
                ctx.ends_turn = True
            return
        if town_store or mesagoza:
            if mesagoza and not (await ctx.flip_coins(1, 'Mesagoza'))[0]:
                return
            cards = await ctx.search_deck(
                is_pokemon_tool if town_store else is_pokemon_card,
                count=1, minimum=0, reveal_result=True,
                prompt='Choose a Pokémon Tool' if town_store else 'Choose a Pokémon')
            await ctx.put_in_hand(cards, reveal=True)
            await ctx.shuffle_deck()
            return
        if heat_factory or discard_search:
            cost = [c for c in ctx.hand() if not heat_factory or energy_provides_type(c, PokemonTypes.FIRE.value)]
            if not cost:
                return
            paid = await ctx.choose_cards(cost, 1, minimum=1, prompt='Choose a card to discard')
            if not paid:
                return
            await ctx.discard_cards(paid)
            if heat_factory:
                await ctx.draw_cards(3)
                return
            fire = 'up to 2 fire energy cards' in t
            predicate = (lambda c: energy_provides_type(c, PokemonTypes.FIRE.value)) if fire else is_basic_energy
            cards = await ctx.search_deck(predicate, count=2 if fire else 1,
                minimum=0, reveal_result=True, prompt='Choose Energy cards')
            await ctx.put_in_hand(cards, reveal=True)
        elif brooklet:
            if len(ctx.my_bench()) >= effective_bench_capacity(ctx.board, ctx.player_id):
                return
            types = {PokemonTypes.WATER.value, PokemonTypes.FIGHTING.value}
            cards = await ctx.search_deck(lambda c: is_basic_pokemon(c) and bool(types.intersection(
                c.get_attribute(AttrID.POKEMON_TYPES) or [])), count=1, minimum=0, prompt='Choose a Basic Water or Fighting Pokémon')
            for card in cards:
                await ctx.bench_pokemon(card)
        elif ultra_space:
            cards = await ctx.search_deck(lambda c: any(s.casefold() == 'ultra beast' for s in subtypes_for(c.archetype_id)),
                count=1, minimum=0, reveal_result=True, prompt='Choose an Ultra Beast')
            await ctx.put_in_hand(cards, reveal=True)
        await ctx.shuffle_deck()

    return effect

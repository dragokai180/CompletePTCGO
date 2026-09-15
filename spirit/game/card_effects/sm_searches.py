"""Ordered SM search effects that cannot use generic search-to-hand."""
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.data_utils import def_for, subtypes_for
from spirit.game.session.effects import is_basic_energy, is_pokemon_card, is_trainer_card
from spirit.game.session.passives import effective_bench_capacity


def name(card):
    return getattr(def_for(getattr(card, 'archetype_id', '')), 'display_name', '') or ''


SEARCH_TITLES = {'Energy Spinner', 'Beast Ring', 'Dusk Stone', 'Rainbow Brush',
                 'Fossil Excavation Map', 'Pokémon Research Lab', 'Red & Blue',
                 'Rosa', 'Lance ◇'}


def immediate_evolution(evolution, pokemon):
    return evolution.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)


async def resolve_sm_search(ctx):
    title = name(ctx.source)
    if title not in SEARCH_TITLES:
        return False
    if search_permission(ctx.board, ctx.player_id, title) is False:
        return True
    if title == 'Rosa':
        groups = [(is_pokemon_card, 1, "Pokémon"),
                  (is_trainer_card, 1, "Trainer"),
                  (is_basic_energy, 1, "Basic Energy")]
        picks = await ctx.search_deck_groups(groups, prompt="Choose cards to reveal")
        await ctx.put_in_hand([c for group in picks for c in group], reveal=True)
        await ctx.shuffle_deck()
    elif title == 'Lance ◇':
        # Lance puts Dragon Pokemon in play, including evolutions. This is
        # not a normal Basic-only play from the hand or an evolution action.
        free = max(0, effective_bench_capacity(ctx.board, ctx.player_id) - len(ctx.my_bench()))
        cards = await ctx.search_deck(
            lambda c: is_pokemon_card(c) and PokemonTypes.DRAGON.value in
            (c.get_attribute(AttrID.POKEMON_TYPES) or []),
            count=min(2, free), minimum=0, prompt="Choose Dragon Pokémon")
        for card in cards:
            await ctx.bench_pokemon(card)
        await ctx.shuffle_deck()
    elif title == 'Energy Spinner':
        first_second = ctx.session.turn_state.turn_number == 2 and ctx.session.first_player_id != ctx.player_id
        cards = await ctx.search_deck(is_basic_energy, 3 if first_second else 1,
                                      minimum=0, reveal_result=True, prompt="Choose Basic Energy cards")
        await ctx.put_in_hand(cards, reveal=True)
        await ctx.shuffle_deck()
    elif title == 'Beast Ring':
        targets = [p for p in ctx.my_pokemon_in_play() if 'Ultra Beast' in (subtypes_for(p.archetype_id) or [])]
        if targets:
            # Choose ONE Ultra Beast; both searched Energy cards go to it.
            target = await ctx.choose_pokemon(targets, "Choose an Ultra Beast")
            cards = await ctx.search_deck(is_basic_energy, 2, minimum=0, prompt="Choose Basic Energy cards")
            if target is not None:
                for card in cards:
                    await ctx.attach_energy(card, target)
            await ctx.shuffle_deck()
    elif title == 'Dusk Stone':
        names = {'Mismagius', 'Mismagius-GX', 'Honchkrow', 'Honchkrow-GX',
                 'Chandelure', 'Chandelure-GX', 'Aegislash', 'Aegislash-GX'}
        targets = list(ctx.my_pokemon_in_play())
        def predicate(card):
            return name(card) in names and any(immediate_evolution(card, p) for p in targets)
        cards = await ctx.search_deck(predicate, 1, minimum=0, prompt="Choose an evolution")
        if cards:
            candidates = [p for p in targets if immediate_evolution(cards[0], p)]
            target = await ctx.choose_pokemon(candidates, "Choose the Pokémon to evolve")
            if target is not None:
                await ctx.evolve_pokemon(target, cards[0])
        await ctx.shuffle_deck()
    elif title == 'Red & Blue':
        from spirit.game.card_effects.trainer_followup import evosoda_targets
        targets = evosoda_targets(ctx.board, ctx.player_id)
        paid = False
        if len([c for c in ctx.hand() if c is not ctx.source]) >= 2 and await ctx.ask_yes_no(
                "Discard 2 cards to attach Basic Energy after evolving?"):
            discarded = await ctx.discard_from_hand(2, minimum=2,
                predicate=lambda c: c is not ctx.source, prompt="Choose 2 cards to discard")
            paid = len(discarded) == 2
        cards = await ctx.search_deck(lambda c: 'GX' in (subtypes_for(c.archetype_id) or [])
            and any(immediate_evolution(c, p) for p in targets), 1, minimum=0,
            prompt="Choose a Pokémon-GX evolution")
        evolved = None
        if cards:
            target = await ctx.choose_pokemon([p for p in targets if immediate_evolution(cards[0], p)],
                                              "Choose the Pokémon to evolve")
            if target is not None and await ctx.evolve_pokemon(target, cards[0]):
                evolved = cards[0]
        await ctx.shuffle_deck()
        if paid and evolved is not None:
            energies = await ctx.search_deck(is_basic_energy, 2, minimum=0,
                                             prompt="Choose Basic Energy cards")
            for energy in energies:
                await ctx.attach_energy(energy, evolved)
            await ctx.shuffle_deck()
    elif title == 'Rainbow Brush':
        holders = {e: p for p in ctx.my_pokemon_in_play() for e in ctx.attached_energies(p)}
        selected = await ctx.choose_cards(list(holders), 1, minimum=1, prompt="Choose Energy to exchange") if holders else []
        if selected:
            cards = await ctx.search_deck(is_basic_energy, 1, minimum=0, prompt="Choose a Basic Energy card")
            if cards:
                await ctx.attach_energy(cards[0], holders[selected[0]])
                await ctx.shuffle_into_deck(selected)
            else:
                await ctx.shuffle_deck()
    elif title == 'Fossil Excavation Map':
        fossils = [c for c in ctx.discard_pile() if name(c) == 'Unidentified Fossil']
        options = []
        if ctx.deck():options.append('Search your deck')
        if fossils:options.append('Recover from discard')
        if options:
            index = await ctx.choose("Choose an effect", options) if len(options) > 1 else 0
            if options[index] == 'Search your deck':
                cards = await ctx.search_deck(lambda c: name(c) == 'Unidentified Fossil',
                                              1, minimum=0, reveal_result=True)
                await ctx.put_in_hand(cards, reveal=True)
                await ctx.shuffle_deck()
            else:
                cards = await ctx.choose_cards(fossils, 1, minimum=1, prompt="Choose Unidentified Fossil")
                await ctx.put_in_hand(cards, reveal=True)
    elif title == 'Pokémon Research Lab':
        available = max(0, effective_bench_capacity(ctx.board, ctx.player_id) - len(ctx.my_bench()))
        def predicate(card):
            return card.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == 'UnidentifiedFossil'
        cards = await ctx.search_deck(predicate, min(2, available), minimum=0,
                                      prompt="Choose Pokémon that evolve from Unidentified Fossil") if available else []
        for card in cards:
            await ctx.bench_pokemon(card)
        await ctx.shuffle_deck()
        ctx.ends_turn = True
    else:
        return False
    return True


def search_permission(board, pid, title):
    if title not in SEARCH_TITLES:
        return None
    def cards(owner, zone):
        area = board.find_player_area(owner, zone)
        return list(area.children) if area is not None else []
    deck = cards(pid, 'deck')
    if title in {'Rosa', 'Lance ◇'}:
        state = getattr(board, 'turn_state', None)
        if not deck or state is None or not state.pokemon_lost_last_turn(pid):
            return False
        return title == 'Rosa' or len(cards(pid, 'bench')) < effective_bench_capacity(board, pid)
    if title == 'Red & Blue':
        from spirit.game.card_effects.trainer_followup import evosoda_targets
        return bool(deck) and bool(evosoda_targets(board, pid))
    if title == 'Dusk Stone':
        return bool(deck) and any(name(p) in {'Misdreavus', 'Murkrow', 'Lampent', 'Doublade'}
                                  for p in board.pokemon_in_play(pid))
    if title == 'Energy Spinner':
        return bool(deck)
    if title == 'Fossil Excavation Map':
        return bool(deck) or any(name(c) == 'Unidentified Fossil' for c in cards(pid, 'discard'))
    if title == 'Rainbow Brush':
        return bool(deck) and any(board.attached_energies(p) for p in board.pokemon_in_play(pid))
    if title == 'Beast Ring':
        opponent = next((p for p in board.player_ids if p != pid), None)
        return bool(deck) and len(cards(opponent, 'prizePile')) in (3, 4) and any(
            'Ultra Beast' in (subtypes_for(p.archetype_id) or []) for p in board.pokemon_in_play(pid))
    return None

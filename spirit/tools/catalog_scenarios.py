"""Positive public-state fixtures for authored effects in the catalog audit.

Never replaces a card's implementation or condition. The caller still checks
the real permission and runs the real effect after these board preparations.
"""
import re
import json

from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage
from spirit.game.data_utils import CARD_DEFS_BY_GUID, PokemonCardDef, EnergyCardDef, PokemonToolCardDef, Ability, def_for
from spirit.game.models.board import create_card_entity
from spirit.game.scripts.cards import loader
from spirit.tools.effect_smoke import P1, P2, _def_attr


def enrich(rig, entities, runner, text):
    board, state = rig.board, rig.session.turn_state
    name = rig.target_def.display_name or ''
    title = runner.title if isinstance(runner, Ability) else ''
    source = entities['p1_active']
    text = text.lower().replace('[d]', 'darkness').replace('[w]', 'water')

    def area(pid, zone): return board.find_player_area(pid, zone)
    def named(d, wanted): return (d.display_name or '').casefold() == wanted.casefold()
    def subtype(d, wanted): return wanted.casefold() in {s.casefold() for s in d.subtypes or []}
    def typed(d, word):
        raw = _def_attr(d, AttrID.POKEMON_TYPES, []) or []
        values = json.loads(raw) if isinstance(raw, str) else raw
        return isinstance(d, PokemonCardDef) and getattr(PokemonTypes, word.upper()).value in values
    def add(pid, zone, predicate):
        d = next((d for d in CARD_DEFS_BY_GUID.values() if predicate(d)), None)
        if d is None: return None
        card = create_card_entity(loader.cards_by_guid[d.guid.lower()], pid)
        board.add_card_to_area(card, area(pid, zone))
        return card
    def active(pid, predicate):
        for old in list(area(pid, 'activePokemonArea').children): rig.to_area(old, pid, 'discard')
        card = add(pid, 'activePokemonArea', predicate)
        if card: entities['p1_active' if pid == P1 else 'p2_active'] = card
        return card
    def energy(holder, kind=PokemonTypes.WATER):
        if holder: rig.attach_energy_type(holder.owning_player_id, holder, kind.value)
    def prize(pid, number):
        pile = area(pid, 'prizePile')
        while len(pile.children) > number: rig.to_area(pile.children[-1], pid, 'deck')
    def subtype_pokemon(wanted): return lambda d: isinstance(d, PokemonCardDef) and subtype(d, wanted)

    if isinstance(rig.target_def, PokemonToolCardDef):
        if title in ('G Booster', 'G Scope'):
            source = active(P1, lambda d: named(d, 'Genesect-EX'))
        elif 'Scroll' in name:
            source = active(P1, subtype_pokemon('Rapid Strike' if 'Rapid Strike' in name else 'Single Strike'))
        elif 'Seal Stone' in name:
            source = active(P1, lambda d: isinstance(d, PokemonCardDef) and subtype(d, 'V')
                            and _def_attr(d, AttrID.STAGE) == PokemonStage.BASIC.value)
        if source:
            board.attach_card(entities['target'].entity_id, source.entity_id)
            for kind in (PokemonTypes.GRASS, PokemonTypes.WATER, PokemonTypes.FIRE):
                for _ in range(3): energy(source, kind)

    if '3 or fewer prize' in text: prize(P2, 3)
    if '2 or fewer prize' in text: prize(P2, 2)
    lost = re.search(r'(\d+) or more cards in (?:the|your) lost zone', text)
    if lost:
        for _ in range(int(lost[1])): add(P1, 'lostZone', lambda d: isinstance(d, EnergyCardDef))
    if name == 'Lost World':
        for _ in range(6): add(P2, 'lostZone', lambda d: isinstance(d, PokemonCardDef))
    if 'pokémon were knocked out' in text or "team rocket's pokémon were knocked out" in text:
        d = next(d for d in CARD_DEFS_BY_GUID.values() if isinstance(d, PokemonCardDef)
                 and (d.display_name or '').startswith("Team Rocket's"))
        record = {'archetype_id': d.guid, 'pokemon_types': [PokemonTypes.DARKNESS.value]}
        state.kos_by_attack_last_turn[P1] = [record]
        state.kos_suffered_last_turn[P1] = [record]
    if 'played a supporter card' in text:
        state.supporter_played = True
        state.supporters_played = 1
        supporter = add(P1, 'discard', lambda d: named(d, "Team Rocket's Giovanni"))
        if supporter: rig.session._record_trainer_played(supporter)
    if 'move a special energy' in text:
        card = add(P1, 'hand', lambda d: isinstance(d, EnergyCardDef) and d.display_name == 'Double Colorless Energy')
        if card: board.attach_card(card.entity_id, source.entity_id)
    if 'tag team pokémon' in text:
        energy(add(P1, 'bench', subtype_pokemon('TAG TEAM')))
    if 'team plasma' in text or title == 'Plasma Transfer':
        add(P1, 'bench', subtype_pokemon('Team Plasma'))
        add(P1, 'discard', lambda d: subtype(d, 'Team Plasma'))
        card = add(P1, 'hand', lambda d: named(d, 'Plasma Energy'))
        if card: board.attach_card(card.entity_id, source.entity_id)
        add(P1, 'deck', lambda d: named(d, 'Plasma Energy'))
    if 'pokemon v' in text.replace('pokémon', 'pokemon'):
        add(P1, 'bench', subtype_pokemon('VMAX' if 'pokémon vmax' in text else 'V'))
        add(P2, 'bench', subtype_pokemon('V'))
    if 'tera pokémon' in text:
        active(P2, subtype_pokemon('Tera'))
    if name in ('Jacinthe', 'Life Forest ◇', 'Crystal Cave', 'Siebold'):
        word = {'Jacinthe': 'psychic', 'Life Forest ◇': 'grass', 'Crystal Cave': 'metal', 'Siebold': 'water'}[name]
        card = add(P1, 'bench', lambda d: typed(d, word) and (name != 'Siebold' or subtype(d, 'Rapid Strike')))
        if card: card.set_attribute(AttrID.HP, 10)
    for word in ('darkness', 'psychic', 'metal', 'fire', 'water'):
        if f'benched {word} pokémon' in text or f'your {word} pokémon' in text:
            add(P1, 'bench', lambda d, word=word: typed(d, word))
        if f'active {word} pokémon' in text:
            active(P1, lambda d, word=word: typed(d, word))
    if title == 'Adrena-Brain': energy(source, PokemonTypes.DARKNESS)
    if title == 'Irresistible Force': energy(board.pokemon_in_play(P1)[-1], PokemonTypes.FIGHTING)
    if "benched n's pokémon" in text:
        add(P1, 'bench', lambda d: isinstance(d, PokemonCardDef) and (d.display_name or '').startswith("N's "))
    if "active team rocket's pokémon" in text:
        predicate = lambda d: isinstance(d, PokemonCardDef) and (d.display_name or '').startswith("Team Rocket's ")
        active(P1, predicate); add(P1, 'bench', predicate)
    if 'fire mega evolution pokémon ex' in text:
        add(P1, 'bench', lambda d: typed(d, 'fire') and 'Mega ' in (d.display_name or '') and subtype(d, 'ex'))
    if name == "Rosa's Encouragement": add(P1, 'bench', lambda d: isinstance(d, PokemonCardDef) and _def_attr(d, AttrID.STAGE) == PokemonStage.STAGE2.value)
    if name in ('Rescue Carrier', 'Summoning Star') or title == 'Summoning Star':
        add(P1, 'discard', lambda d: isinstance(d, PokemonCardDef) and _def_attr(d, AttrID.HP, 999) <= 90 and typed(d, 'colorless') and not subtype(d, 'V'))
    if title == 'Phantom Transformation':
        add(P1, 'discard', lambda d: isinstance(d, PokemonCardDef) and _def_attr(d, AttrID.STAGE) == PokemonStage.STAGE1.value and not named(d, 'Zoroark'))
    if name == 'Professor Laventon': add(P1, 'discard', lambda d: isinstance(d, PokemonCardDef) and 'Hisuian' in (d.display_name or ''))
    if name == 'Welcoming Lantern': add(P1, 'discard', lambda d: subtype(d, 'Single Strike') and 'Supporter' in (d.subtypes or []))
    if title == 'Sketching Trash': add(P1, 'discard', lambda d: subtype(d, 'Fusion Strike') and 'Item' in (d.subtypes or []))
    if name in ('Pokémon Ranger', 'Channeler'):
        state.lock_retreat(source.entity_id)
    if name in ('Dusk Stone', 'Rare Candy'):
        from spirit.game.data_utils import evolves_from, evolves_from_chain
        stage2 = next(d for d in CARD_DEFS_BY_GUID.values() if isinstance(d, PokemonCardDef)
                      and (named(d, 'Chandelure') if name == 'Dusk Stone' else named(d, 'Blastoise')))
        add(P1, 'deck' if name == 'Dusk Stone' else 'hand', lambda d: d is stage2)
        add(P1, 'bench', lambda d: isinstance(d, PokemonCardDef)
            and (_def_attr(d, AttrID.EVOLUTION_LOGIC_NAME) == _def_attr(stage2, AttrID.EVOLUTION_LOGIC_FROM) if name == 'Dusk Stone' else
                 _def_attr(d, AttrID.STAGE) == PokemonStage.BASIC.value and evolves_from(stage2.guid, _def_attr(d, AttrID.EVOLUTION_LOGIC_NAME))))
    for wanted in ('Lunatone', 'Solrock', 'Latias', 'Latios', 'Articuno', 'Zapdos', 'Moltres',
                   'Regirock', 'Regice', 'Registeel', 'Regieleki', 'Regidrago'):
        if wanted.lower() in text and not named(rig.target_def, wanted):
            add(P1, 'bench', lambda d, wanted=wanted: named(d, wanted))
    if title == 'Oceanic Accompaniment':
        add(P1, 'bench', lambda d: isinstance(d, PokemonCardDef) and any(a.title == 'Swim Freely' for a in d.abilities))
    if title == 'Boom Boom Groove':
        active(P1, lambda d: isinstance(d, PokemonCardDef) and any(a.title == 'Festival Lead' for a in d.abilities))
    if title == 'Elusive Master':
        for card in list(area(P1, 'hand').children): rig.to_area(card, P1, 'deck')
        rig.to_area(entities['target'], P1, 'hand')
    if name == 'Cheryl':
        card = add(P1, 'bench', lambda d: isinstance(d, PokemonCardDef) and _def_attr(d, AttrID.STAGE) == PokemonStage.STAGE1.value)
        if card: card.set_attribute(AttrID.HP, 10)
    if name == 'Urn of Vitality': add(P1, 'discard', lambda d: named(d, 'Single Strike Energy'))
    if title == 'Scrounge': add(P1, 'discard', lambda d: isinstance(d, PokemonToolCardDef))
    if title == 'Purifying Fire': energy(source, PokemonTypes.FIRE)
    if name == "N's Plan": energy(board.pokemon_in_play(P1)[-1])
    if name == 'Full Heal': entities['p1_active'].set_attribute(AttrID.SPECIAL_CONDITIONS, ['Asleep'])
    if name == 'All-Night Party': entities['p1_active'].set_attribute(AttrID.SPECIAL_CONDITIONS, ['Asleep'])
    if name == 'Toy Catcher': board.pokemon_in_play(P2)[-1].set_attribute(AttrID.HP, 30)
    if name == 'Ruffian':
        target = entities['p2_active']
        for predicate in (lambda d: isinstance(d, PokemonToolCardDef),
                          lambda d: isinstance(d, EnergyCardDef) and named(d, 'Double Colorless Energy')):
            card = add(P2, 'hand', predicate)
            if card: board.attach_card(card.entity_id, target.entity_id)
    if title == 'Pheromone Poison': add(P1, 'bench', lambda d: named(d, 'Nidoran ♀'))
    if title in ('Fully Singe', 'Grass Fire'):
        energy(entities['p2_active'], PokemonTypes.GRASS)
    if title == 'Imittack':
        for kind in (PokemonTypes.GRASS, PokemonTypes.WATER, PokemonTypes.FIRE):
            for _ in range(5): energy(source, kind)
    if title == 'Bad-Influence Evolution':
        add(P1, 'bench', lambda d: typed(d, 'darkness'))
        add(P1, 'deck', lambda d: named(d, 'Pangoro'))
    if title == 'Digital Reboot':
        top = add(P1, 'bench', lambda d: named(d, 'Wartortle'))
        base = add(P1, 'hand', lambda d: named(d, 'Squirtle'))
        if top and base: board.attach_card(base.entity_id, top.entity_id)
    if title == 'Primordial Boom':
        for stadium in board.find_global_area('activeStadium').children:
            stadium.owning_player_id = P2
    if title in ('Sudden Grip', 'Sudden Sting', 'Tentavolve'):
        wanted = {'Sudden Grip': 'Shellder', 'Sudden Sting': 'Kakuna', 'Tentavolve': 'Tentacool'}[title]
        card = add(P1, 'hand', lambda d: named(d, wanted))
        if card: board.attach_card(card.entity_id, source.entity_id)
        state.entered_play_turn[source.entity_id] = state.turn_number
    if title == 'Improvisational Performance':
        while len(area(P1, 'hand').children) > 3: rig.to_area(area(P1, 'hand').children[0], P1, 'deck')
        while len(area(P1, 'hand').children) < 3: add(P1, 'hand', lambda d: isinstance(d, EnergyCardDef))
    if title == 'Transfer Junk':
        for wanted in ('Lugia-EX', 'Colress', 'Plasma Energy'):
            add(P1, 'discard', lambda d, wanted=wanted: named(d, wanted) and subtype(d, 'Team Plasma'))
    if title == 'Signs of Evolution':
        for wanted in ('Vaporeon', 'Jolteon', 'Flareon'): add(P1, 'deck', lambda d, wanted=wanted: named(d, wanted))
    if title == "Moon's Invite":
        old_choice = rig.session.prompt_choice_panel
        async def positive_count(pid, source, buttons, prompt, *args, **kwargs):
            if 'How many damage counters' in prompt: return 1
            return await old_choice(pid, source, buttons, prompt, *args, **kwargs)
        rig.session.prompt_choice_panel = positive_count
    prior = re.search(r'1 of your (.+?) used (.+?) during your last turn', text)
    if prior:
        card = add(P1, 'bench', lambda d: named(d, prior[1]))
        if card:
            attack = next((a for d in CARD_DEFS_BY_GUID.values() for a in getattr(d, 'abilities', [])
                           if a.title.casefold() == prior[2]), None)
            state.attacks_prev_turn_by_player[P1] = [(card.entity_id, card.archetype_id, attack.title if attack else prior[2])]
    own_prior = re.search(r'this pokémon used (.+?) during your last turn', text)
    if own_prior:
        attack = next((a for a in rig.target_def.abilities if a.title.casefold() == own_prior[1]), None)
        if attack: state.attacks_prev_turn_by_player[P1] = [(source.entity_id, source.archetype_id, attack.title)]

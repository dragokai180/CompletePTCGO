"""Exercise every overridden Passive hook, grouped by implementation and text.

This is interface/runtime coverage, not proof that every conditional branch
matches its printed rule. Each async event receives an isolated board. Sync
hooks are also exercised against an opposing Pokemon/player.
"""
import argparse
import asyncio
import inspect
import json
from collections import Counter
from pathlib import Path

from spirit.game.attributes import AttrID, PokemonTypes, SpecialConditions, TrainerType
from spirit.game.data_utils import (
    CARD_DEFS_BY_GUID, Ability, Attack, PokemonCardDef, EnergyCardDef, StadiumCardDef,
)
from spirit.game.scripts.cards import loader
from spirit.game.session.effects import EffectContext, full_stack, is_energy_card
from spirit.game.session.game_session import GameOver
from spirit.game.session.passives import Passive, DamageCalc
from spirit.tools.catalog_campaign import tree_errors
from spirit.tools.effect_smoke import Rig, P1, P2, pick_filler_basic, pick_filler_item, basic_energy_guids
from spirit.tools.semantic_effect_audit import _semantic_scenario


def families():
    grouped = {}
    for definition in {d.guid: d for d in CARD_DEFS_BY_GUID.values()}.values():
        entries = [(getattr(definition, 'passive', None), '', None)]
        entries += [(a.passive, a.game_text or '', a) for a in getattr(definition, 'abilities', []) if a.passive]
        for passive, text, ability in entries:
            if passive is None:
                continue
            text = text or getattr(passive, 'text', '')
            key = (type(passive).__module__, type(passive).__qualname__, text, repr(vars(passive)))
            entry = grouped.setdefault(key, [definition, passive, text, ability, []])
            entry[4].append(definition.guid)
    return list(grouped.values())


def prepare(definition, passive, text, ability, filler, energies, item):
    rig = Rig(definition, filler, energies, item)
    kind = 'pokemon' if isinstance(definition, PokemonCardDef) else 'energy' if isinstance(definition, EnergyCardDef) else 'trainer'
    entities = rig.setup(kind)
    setup = _semantic_scenario('ability', text.lower())
    if setup:
        setup(rig, entities, ability or 'passive')
    board = rig.board
    carrier = entities['target']
    own, other = entities['p1_active'], entities['p2_active']
    if not isinstance(definition, PokemonCardDef):
        if isinstance(definition, StadiumCardDef):
            board.move_card(carrier.entity_id, board.find_global_area('activeStadium').entity_id)
            carrier.owning_player_id = P1
        else:
            board.attach_card(carrier.entity_id, own.entity_id)
    return rig, carrier, own, other


def arguments(rig, carrier, own, other, opponent=False):
    board = rig.board
    target = other if opponent else own
    pid = target.owning_player_id
    attack = Attack(title='Audit attack', cost={PokemonTypes.COLORLESS: 1}, damage=50)
    ctx = EffectContext(rig.session, pid, target, attack)
    # Some positive shield fixtures intentionally replace the Active with an
    # unpowered Pokemon. An Energy argument must not assume an attachment.
    energy = next(iter(board.attached_energies(target)), None)
    if energy is None:
        energy = next(c for c in ctx.hand() if is_energy_card(c))
    tool = next((c for c in full_stack(carrier) if c.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.POKEMON_TOOL.value), carrier)
    ctx.energy_receiver = target
    ctx.attached_energy = energy
    ctx.attaching_player_id = pid
    ctx.attached_tool = tool
    ctx.benched_pokemon = target
    ctx.evolved_pokemon = target
    ctx.evolved_from = target
    ctx.new_active = target
    ctx.previous_active = None
    ctx.switch_reason = 'retreat'
    ctx.knocked_out_pokemon = target
    ctx.knocked_out_stack = list(full_stack(target))
    ctx.knocked_out_attachments = ctx.knocked_out_stack[1:]
    ctx.knocked_out_types = target.get_attribute(AttrID.POKEMON_TYPES) or []
    ctx.knocked_out_energy_types = [PokemonTypes.WATER.value]
    ctx.knocked_out_retreat_cost = target.get_attribute(AttrID.RETREAT_COST) or 0
    ctx.attack_damage = {target.entity_id: (30, 100)}
    ctx.attack_damage_active = {target.entity_id}
    ctx.coin_results = [False]
    return dict(board=board, carrier=carrier, pokemon=target, target=target,
                attacker=own if opponent else other, holder=target, energy=energy,
                tool=tool, card=target, trainer_card=tool, trainer_type=TrainerType.ITEM.value,
                player_id=pid, affected_player_id=pid, attaching_player_id=pid,
                mover_player_id=pid, affected_entity=target, evolution_card=target,
                evolved=target, pre_evolution=target, ability=attack, attack=attack,
                ctx=ctx, calc=DamageCalc(board, other if not opponent else own, target, 50),
                count=1, counters=1, coins=1, condition=SpecialConditions.POISONED,
                options=[[PokemonTypes.WATER.value]], types=[PokemonTypes.WATER.value])


async def main_async(args):
    loader.load_all()
    filler, energies, item = pick_filler_basic(), basic_energy_guids(), pick_filler_item()
    groups, rows = families(), []
    if args.retry_report:
        previous = json.loads(args.retry_report.read_text(encoding='utf8'))
        wanted = {guid for row in previous if row['status'] != 'PASS' for guid in row['printings']}
        groups = [group for group in groups if wanted.intersection(group[4])]
    names = [name for name, value in vars(Passive).items() if callable(value)]
    names += ['damage_interceptor', 'attack_followup']
    for index, (definition, passive, text, ability, printings) in enumerate(groups, 1):
        rig = None
        hooks = [name for name in names if callable(getattr(passive, name, None))
                 and getattr(type(passive), name, None) is not getattr(Passive, name, None)]
        for hook in hooks:
            fn = getattr(passive, hook)
            scopes = (False,) if inspect.iscoroutinefunction(fn) else (False, True)
            for opponent in scopes:
                status, detail = 'PASS', ''
                try:
                    if rig is None or inspect.iscoroutinefunction(fn):
                        if rig:
                            rig.session.cleanup()
                        rig, carrier, own, other = prepare(definition, passive, text, ability, filler, energies, item)
                    values = arguments(rig, carrier, own, other, opponent)
                    values['cost'] = {'Water': 1, 'Colorless': 2} if hook.startswith('modify_attack_cost') else 3
                    signature = inspect.signature(fn)
                    kwargs = {p: values[p] for p in signature.parameters}
                    result = fn(**kwargs)
                    if inspect.isawaitable(result):
                        await asyncio.wait_for(result, 3)
                    errors = tree_errors(rig.board)
                    if errors:
                        raise AssertionError(errors)
                except GameOver:
                    pass
                except Exception as exc:
                    status, detail = 'FAIL', f'{type(exc).__name__}: {exc}'
                rows.append(dict(card=definition.display_name, set=definition.set_code,
                                 number=definition.collector_number, text=text, hook=hook,
                                 opponent=opponent, printings=printings, status=status, detail=detail))
                if inspect.iscoroutinefunction(fn) and rig:
                    rig.session.cleanup()
                    rig = None
        if rig:
            rig.session.cleanup()
        if index % 50 == 0:
            print(index, '/', len(groups), dict(Counter(r['status'] for r in rows)), flush=True)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding='utf8')
    print('families', len(groups), 'hooks', len(rows), dict(Counter(r['status'] for r in rows)))
    return int(any(row['status'] != 'PASS' for row in rows))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json', type=Path, required=True)
    parser.add_argument('--retry-report', type=Path)
    raise SystemExit(asyncio.run(main_async(parser.parse_args())))

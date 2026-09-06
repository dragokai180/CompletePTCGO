import { getPrefabById } from '../prefabs/catalog';
import {
  matchEffectTextPartial,
  matchSingleClause,
  matchedToSelected,
  splitTrainerClauses,
} from '../prefabs/matcher';
import { findServerEffects } from '../serverEffects';
import type { SelectedPrefab, ServerEffect } from '../types';
import { effectFnName } from './effectFnName';
import { isTrainerReminderText, stripTrainerReminders } from '../trainerReminders';

const FULL_TEXT_REUSE = 0.92;
const CLAUSE_REUSE = 0.85;

function wrapDocstring(text: string, indent = '    ', width = 72): string {
  const words = text.replace(/\s+/g, ' ').trim().split(' ').filter(Boolean);
  const lines: string[] = [];
  let current = '';
  for (const word of words) {
    const next = current ? `${current} ${word}` : word;
    if (current && next.length > width) {
      lines.push(current);
      current = word;
    } else {
      current = next;
    }
  }
  if (current) lines.push(current);
  if (lines.length <= 1) return `"""${lines[0] || ''}"""`;
  return `"""${lines[0]}\n${lines.slice(1).map(l => indent + l).join('\n')}"""`;
}

function awaitCall(effectExpr: string): string {
  const trimmed = effectExpr.trim();
  return `await ${trimmed}(ctx)`;
}

function renamePythonIdent(source: string, from: string, to: string): string {
  if (!from || from === to) return source;
  const escaped = from.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  return source
    .replace(new RegExp(`\\b${escaped}\\b`, 'g'), to)
    .replace(new RegExp(`_${escaped}\\b`, 'g'), `_${to}`);
}

function uniqueFnName(base: string, used: Set<string>): string {
  let name = base;
  let n = 2;
  while (used.has(name)) {
    name = `${base}_${n}`;
    n += 1;
  }
  used.add(name);
  return name;
}

interface TrainerPiece {
  clause: string;
  prefab?: SelectedPrefab;
  server?: ServerEffect;
}

function pieceHelpers(piece: TrainerPiece): string[] {
  if (piece.server?.helpers?.length) {
    return piece.server.helpers.filter(h => /^(async\s+)?def\s+/.test(h.trim()));
  }
  if (!piece.prefab) return [];
  const prefab = getPrefabById(piece.prefab.prefabId);
  if (!prefab) return [];
  return (prefab.generateCall(piece.prefab.params, { kind: 'trainer', index: 0 }).helpers || [])
    .filter(Boolean);
}

function pieceImports(piece: TrainerPiece): string[] {
  if (piece.server?.imports?.length) return piece.server.imports;
  if (!piece.prefab) return [];
  const prefab = getPrefabById(piece.prefab.prefabId);
  if (!prefab) return [];
  const result = prefab.generateCall(piece.prefab.params, { kind: 'trainer', index: 0 });
  const out: string[] = [];
  for (const imp of result.imports || []) {
    if (!imp.module || !imp.names?.length) continue;
    out.push(`from ${imp.module} import ${imp.names.join(', ')}`);
  }
  return out;
}

function pieceEffectExpr(piece: TrainerPiece): string | undefined {
  if (piece.server) {
    const body = (piece.server.body || []).filter(Boolean);
    const joined = body.join('\n').trim();
    const exprMatch = joined.match(/^effect\s*=\s*(.+)$/m);
    return exprMatch ? exprMatch[1].trim() : body.length === 1 ? body[0].trim() : undefined;
  }
  if (piece.prefab) {
    const prefab = getPrefabById(piece.prefab.prefabId);
    return prefab?.generateCall(piece.prefab.params, { kind: 'trainer', index: 0 }).effectExpr;
  }
  return undefined;
}

function pieceCondition(piece: TrainerPiece): string | undefined {
  if (piece.server?.condition) return piece.server.condition;
  if (piece.prefab) {
    const prefab = getPrefabById(piece.prefab.prefabId);
    return prefab?.generateCall(piece.prefab.params, { kind: 'trainer', index: 0 }).condition;
  }
  return undefined;
}

function composeHelper(
  cardName: string,
  text: string,
  pieces: TrainerPiece[]
): { effectExpr: string; helpers: string[]; imports: string[]; condition?: string; sources: string[] } {
  const fnName = effectFnName(cardName);
  const used = new Set<string>([fnName]);
  const helpers: string[] = [];
  const imports: string[] = [];
  const sources: string[] = [];
  const bodyLines: string[] = [];
  const conditions = new Set<string>();

  for (const piece of pieces) {
    imports.push(...pieceImports(piece));
    const cond = pieceCondition(piece);
    if (cond) conditions.add(cond.trim());
    if (piece.server?.source) sources.push(piece.server.source);
    else if (piece.prefab) sources.push(piece.prefab.prefabId);

    const expr = pieceEffectExpr(piece);
    if (!expr) {
      if (cond) continue;
      if (!isTrainerReminderText(piece.clause)) {
        bodyLines.push(`    # Unmatched clause: ${JSON.stringify(piece.clause)}`);
      }
      continue;
    }

    const prefabHelpers = piece.prefab ? pieceHelpers(piece) : [];
    for (const helper of prefabHelpers) {
      helpers.push(helper.trimEnd());
    }

    const localHelpers = (piece.server?.helpers || []).filter(h => /^(async\s+)?def\s+/.test(h.trim()));
    if (localHelpers.length && /^[a-z_][a-z0-9_]*$/i.test(expr)) {
      const renamed = uniqueFnName(expr === fnName ? `_${expr}` : expr, used);
      for (const helper of localHelpers) {
        helpers.push(renamePythonIdent(helper, expr, renamed).trimEnd());
      }
      bodyLines.push(`    ${awaitCall(renamed)}`);
    } else {
      bodyLines.push(`    ${awaitCall(expr)}`);
    }
  }

  const uniqueImports = [...new Set(imports)];
  const docstring = wrapDocstring(text.replace(/\s+/g, ' ').trim());
  const composed = [`async def ${fnName}(ctx):`, `    ${docstring}`, ...bodyLines].join('\n');
  helpers.push(composed);

  return {
    effectExpr: fnName,
    helpers,
    imports: uniqueImports,
    condition: conditions.size === 1 ? [...conditions][0] : undefined,
    sources: [...new Set(sources)],
  };
}

function prefabsToServerIfMultiple(
  cardName: string,
  text: string,
  prefabs: SelectedPrefab[]
): { prefabs: SelectedPrefab[]; serverEffect?: ServerEffect } | null {
  if (prefabs.length <= 1) return null;
  const pieces: TrainerPiece[] = prefabs.map(prefab => ({
    clause: '',
    prefab,
  }));
  const exprs = pieces.map(pieceEffectExpr).filter(Boolean);
  const unique = new Set(exprs);
  if (unique.size <= 1 && exprs.length === prefabs.length) return null;
  const composed = composeHelper(cardName, text, pieces);
  return {
    prefabs: [],
    serverEffect: {
      source: composed.sources.join(' + ') || 'composed',
      effectText: text,
      kind: 'trainer',
      body: [composed.effectExpr],
      imports: composed.imports,
      similarity: 1,
      helpers: composed.helpers,
      condition: composed.condition,
      sources: composed.sources,
    },
  };
}

export async function resolveTrainerEffect(
  text: string,
  cardName: string
): Promise<{ prefabs: SelectedPrefab[]; serverEffect?: ServerEffect }> {
  const trimmed = stripTrainerReminders(text);
  if (!trimmed) return { prefabs: [] };

  const partial = matchEffectTextPartial(trimmed, 'trainer');
  if (partial.matched.length && partial.unmatched.length === 0) {
    const prefabs = matchedToSelected(partial.matched);
    const multi = prefabsToServerIfMultiple(cardName, trimmed, prefabs);
    if (multi) return multi;
    return { prefabs };
  }

  const fullHits = await findServerEffects(trimmed, 'trainer', { minScore: FULL_TEXT_REUSE, limit: 3 });
  if (fullHits[0] && fullHits[0].similarity >= FULL_TEXT_REUSE) {
    return { prefabs: [], serverEffect: { ...fullHits[0], sources: [fullHits[0].source] } };
  }

  const clauses = splitTrainerClauses(trimmed);
  const pieces: TrainerPiece[] = [];
  for (const clause of clauses) {
    const prefabHit = matchSingleClause(clause, 'trainer');
    if (prefabHit) {
      pieces.push({ clause, prefab: matchedToSelected([prefabHit])[0] });
      continue;
    }
    const similar = await findServerEffects(clause, 'trainer', { minScore: CLAUSE_REUSE, limit: 1 });
    if (similar[0]) {
      pieces.push({ clause, server: similar[0] });
      continue;
    }
    pieces.push({ clause });
  }

  const matchedCount = pieces.filter(p => p.prefab || p.server).length;
  if (matchedCount === 0) {
    if (fullHits[0]) return { prefabs: [], serverEffect: { ...fullHits[0], sources: [fullHits[0].source] } };
    return { prefabs: [] };
  }

  if (matchedCount === 1 && pieces.length === 1) {
    const only = pieces[0];
    if (only.prefab) return { prefabs: [only.prefab] };
    if (only.server) return { prefabs: [], serverEffect: { ...only.server, sources: [only.server.source] } };
  }

  const composed = composeHelper(cardName, trimmed, pieces);
  return {
    prefabs: [],
    serverEffect: {
      source: composed.sources.join(' + ') || 'composed',
      effectText: trimmed,
      kind: 'trainer',
      body: [composed.effectExpr],
      imports: composed.imports,
      similarity: matchedCount / pieces.length,
      helpers: composed.helpers,
      condition: composed.condition,
      sources: composed.sources,
    },
  };
}

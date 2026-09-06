import { PREFAB_CATALOG, getPrefabById, prefabsForScope } from './catalog';
import { isTrainerReminderText } from '../trainerReminders';
import type { EffectKind, MatchedPrefab, PrefabDefinition, PrefabScope, SelectedPrefab } from '../types';

export class MissingPrefabError extends Error {
  constructor(text: string) {
    super(`cannot generate - missing prefab\n\nNo prefab found for effect text:\n"${text}"`);
    this.name = 'MissingPrefabError';
  }
}

/** Normalize card text for pattern matching. */
export function normalizeEffectText(text: string): string {
  return text
    .normalize('NFKD')
    .replace(/[\u0300-\u036f]/g, '')
    .replace(/[’‘]/g, "'")
    .replace(/[“”]/g, '"')
    .replace(/Pokémon/gi, 'Pokemon')
    .replace(/\s+/g, ' ')
    .trim();
}

/**
 * Split effect text into matchable clauses.
 * Prefers full-text compound matches first; falls back to sentence segments.
 */
function splitClauses(normalized: string): string[] {
  // Keep common compound openers together — matcher tries full text first.
  const parts = normalized
    .split(/(?<=\.)\s+/)
    .map(s => s.trim())
    .filter(Boolean);
  return parts.length > 0 ? parts : [normalized];
}

function tryMatchPrefab(
  clause: string,
  prefab: PrefabDefinition
): MatchedPrefab | null {
  for (const pattern of prefab.patterns) {
    const match = clause.match(pattern);
    if (!match) continue;

    const params: Record<string, string> = {};
    for (const p of prefab.params) {
      if (p.defaultValue !== undefined) {
        params[p.key] = String(p.defaultValue);
      }
    }
    if (prefab.paramCaptures) {
      for (const [groupIdx, key] of Object.entries(prefab.paramCaptures)) {
        const captured = match[Number(groupIdx)];
        if (captured !== undefined) {
          params[key] = captured;
        }
      }
    }
    // First DRAW_CARDS pattern has no capture — leave default 1
    if (prefab.id === 'DRAW_CARDS' && !match[1]) {
      params.count = '1';
    }
    if (prefab.id === 'DISCARD_X_ENERGY_FROM_THIS_POKEMON' && !match[1]) {
      params.count = '1';
    }

    return { prefab, params, matchedText: clause };
  }
  return null;
}

function catalogForScope(scope: EffectKind): PrefabDefinition[] {
  return prefabsForScope(scope);
}

function pushPrefab(
  results: MatchedPrefab[],
  catalog: PrefabDefinition[],
  id: string,
  params: Record<string, string>,
  matchedText: string
): void {
  const prefab = catalog.find(p => p.id === id);
  if (!prefab) return;
  results.push({ prefab, params, matchedText });
}

/**
 * Strip once-per-turn / evolve / Active Spot framing before matching the remainder.
 * Evolve/on-play must be detected before "Once during your turn" is peeled off,
 * or leftover evolve text is treated as a once-per-turn Ability.
 */
function stripPowerFraming(
  normalized: string,
  catalog: PrefabDefinition[]
): { results: MatchedPrefab[]; remainder: string } {
  const results: MatchedPrefab[] = [];
  let text = normalized;

  const sharedNamed = text.match(
    /^(.*?)\s*you can'?t use more than 1 ability that has ["'](.+?)["'] in its name each turn\.?$/i
  );
  const shared = !sharedNamed
    ? text.match(/^(.*?)\s*you can'?t use more than 1 (.+?) ability each turn\.?$/i)
    : null;
  if (sharedNamed) {
    text = (sharedNamed[1] || '').replace(/[.,;]+\s*$/, '').trim();
    pushPrefab(results, catalog, 'SHARED_ONCE_PER_TURN', { name: (sharedNamed[2] || '').trim() }, sharedNamed[0]);
  } else if (shared) {
    text = (shared[1] || '').replace(/[.,;]+\s*$/, '').trim();
    pushPrefab(results, catalog, 'SHARED_ONCE_PER_TURN', { name: (shared[2] || '').trim() }, shared[0]);
  }

  const evolve = text.match(
    /^(?:once during your turn,?\s*)?when you play this pok[eé]mon from your hand to evolve 1 of your pok[eé]mon(?: during your turn)?,?\s*(?:you may(?: use this ability\.?)?\s*)?(.*)$/i
  );
  const onPlay = !evolve
    ? text.match(
        /^(?:once during your turn,?\s*)?when you play this pok[eé]mon from your hand onto your bench(?: during your turn)?,?\s*(?:you may(?: use this ability\.?)?\s*)?(.*)$/i
      )
    : null;

  if (evolve) {
    pushPrefab(results, catalog, 'ON_EVOLVE', {}, 'when you play this Pokemon from your hand to evolve');
    text = (evolve[1] || '').replace(/^[.,:;]+\s*/, '').trim();
  } else if (onPlay) {
    pushPrefab(results, catalog, 'ON_PLAY', {}, 'when you play this Pokemon from your hand onto your Bench');
    text = (onPlay[1] || '').replace(/^[.,:;]+\s*/, '').trim();
  } else {
    const active = text.match(
      /^(once during your turn,?\s*)?if this pok[eé]mon is in the active spot,?\s*(?:you may(?: use this ability\.?)?\s*)?(.*)$/i
    );
    if (active) {
      pushPrefab(results, catalog, 'IN_ACTIVE_SPOT', {}, 'if this Pokemon is in the Active Spot');
      const oncePrefix = active[1] || '';
      text = `${oncePrefix}${(active[2] || '').trim()}`.replace(/^[.,:;]+\s*/, '').trim();
    }

    const once = text.match(/^once during your turn\.?(?:\s*[,:])?\s*(.*)$/i);
    if (once) {
      pushPrefab(results, catalog, 'USE_ABILITY_ONCE_PER_TURN', { marker: 'ABILITY_USED_MARKER' }, 'Once during your turn.');
      text = (once[1] || '').replace(/^[.,:;]+\s*/, '').trim();
    }
  }

  text = text.replace(/^you may use this ability\.?\s*/i, '').trim();
  return { results, remainder: text };
}

/**
 * Match effect text against the prefab catalog.
 * Empty / whitespace-only text is treated as "no effect" (OK).
 * Throws MissingPrefabError if any clause cannot be matched.
 */
export function matchEffectText(
  text: string,
  scope: EffectKind
): MatchedPrefab[] {
  let normalized = normalizeEffectText(text);
  if (!normalized) {
    return [];
  }

  const catalog = catalogForScope(scope);
  const results: MatchedPrefab[] = [];

  if (scope === 'power') {
    const stripped = stripPowerFraming(normalized, catalog);
    results.push(...stripped.results);
    normalized = stripped.remainder;
    if (!normalized) {
      return results;
    }
  }

  // 1) Try full-text match against longer/compound patterns first
  for (const prefab of catalog) {
    const hit = tryMatchPrefab(normalized, prefab);
    if (hit) {
      return [...results, hit];
    }
  }

  // 2) Split into clauses and match each
  const clauses = splitClauses(normalized);
  if (clauses.length === 1 && results.length === 0) {
    throw new MissingPrefabError(text.trim());
  }
  if (clauses.length === 1 && results.length > 0) {
    // Had "once during your turn" prefix but remainder unmatched
    throw new MissingPrefabError(normalized);
  }

  for (const clause of clauses) {
    let found: MatchedPrefab | null = null;
    for (const prefab of catalog) {
      found = tryMatchPrefab(clause, prefab);
      if (found) break;
    }
    if (!found) {
      throw new MissingPrefabError(clause);
    }
    results.push(found);
  }
  return results;
}

export function splitTrainerClauses(text: string): string[] {
  const normalized = normalizeEffectText(text);
  if (!normalized) return [];
  const parts = normalized
    .split(/(?<=\.)\s+/)
    .map(s => s.trim())
    .filter(Boolean);
  const continuation =
    /^(if you do\b|if heads\b|if tails\b|then\b|shuffle (the|your)\b|otherwise\b)/i;
  const merged: string[] = [];
  for (const part of parts) {
    if (merged.length && continuation.test(part)) {
      merged[merged.length - 1] = `${merged[merged.length - 1]} ${part}`;
    } else {
      merged.push(part);
    }
  }
  const clauses = (merged.length ? merged : [normalized]).filter(c => !isTrainerReminderText(c));
  return clauses;
}

export function matchSingleClause(clause: string, scope: EffectKind): MatchedPrefab | null {
  const catalog = catalogForScope(scope);
  for (const prefab of catalog) {
    const hit = tryMatchPrefab(clause, prefab);
    if (hit) return hit;
  }
  return null;
}

/**
 * Match as much trainer (or other) text as possible without throwing.
 * Full-text prefab hits win; otherwise each clause is tried independently.
 */
export function matchEffectTextPartial(
  text: string,
  scope: EffectKind
): { matched: MatchedPrefab[]; unmatched: string[] } {
  const normalized = normalizeEffectText(text);
  if (!normalized) return { matched: [], unmatched: [] };

  const catalog = catalogForScope(scope);
  for (const prefab of catalog) {
    const hit = tryMatchPrefab(normalized, prefab);
    if (hit) return { matched: [hit], unmatched: [] };
  }

  const clauses = scope === 'trainer' ? splitTrainerClauses(normalized) : splitClauses(normalized);
  const matched: MatchedPrefab[] = [];
  const unmatched: string[] = [];
  for (const clause of clauses) {
    const hit = matchSingleClause(clause, scope);
    if (hit) matched.push(hit);
    else unmatched.push(clause);
  }
  return { matched, unmatched };
}

export function matchedToSelected(matched: MatchedPrefab[]): SelectedPrefab[] {
  return matched.map((m, i) => ({
    id: `${m.prefab.id}-${i}-${Date.now()}`,
    prefabId: m.prefab.id,
    params: { ...m.params },
    source: 'matched' as const,
  }));
}

export function createManualSelected(prefabId: string): SelectedPrefab | null {
  const prefab = getPrefabById(prefabId);
  if (!prefab) return null;
  const params: Record<string, string> = {};
  for (const p of prefab.params) {
    if (p.defaultValue !== undefined) {
      params[p.key] = String(p.defaultValue);
    } else {
      params[p.key] = '';
    }
  }
  return {
    id: `${prefabId}-manual-${Date.now()}`,
    prefabId,
    params,
    source: 'manual',
  };
}

export function listCatalog(scope?: PrefabScope): PrefabDefinition[] {
  if (!scope) return PREFAB_CATALOG;
  if (scope === 'both') return PREFAB_CATALOG;
  return prefabsForScope(scope);
}

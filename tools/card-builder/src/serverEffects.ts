import { effectConstraintsMismatch } from './prefabs/effectAccuracy';
import type { EffectKind, ServerEffect } from './types';

let cached: ServerEffect[] | null = null;

export function normalizeEffectCorpus(text: string): string {
  return text
    .normalize('NFKD')
    .replace(/[\u0300-\u036f]/g, '')
    .replace(/[’‘]/g, "'")
    .replace(/Pokémon/gi, 'Pokemon')
    .replace(/[^a-z0-9]+/gi, ' ')
    .trim()
    .toLowerCase();
}

function similarity(left: string, right: string): number {
  const a = new Set(normalizeEffectCorpus(left).split(/\s+/).filter(Boolean));
  const b = new Set(normalizeEffectCorpus(right).split(/\s+/).filter(Boolean));
  if (a.size === 0 || b.size === 0) return 0;
  let overlap = 0;
  for (const token of a) if (b.has(token)) overlap++;
  return overlap / Math.max(a.size, b.size);
}

/** Jaccard similarity with hard rejects for mismatched numbers, types, and constraints. */
export function scoreEffectTexts(query: string, candidate: string): number {
  if (effectConstraintsMismatch(query, candidate)) return 0;
  return similarity(query, candidate);
}

export async function loadServerEffects(): Promise<ServerEffect[]> {
  if (cached) return cached;
  const response = await fetch('/server-card-effects.json');
  if (!response.ok) {
    throw new Error(`Failed to load server card effects (${response.status})`);
  }
  cached = (await response.json()) as ServerEffect[];
  return cached;
}

export async function findServerEffects(
  text: string,
  kind?: EffectKind,
  opts?: { minScore?: number; limit?: number }
): Promise<ServerEffect[]> {
  if (!text.trim()) return [];
  const minScore =
    opts?.minScore ?? (kind === 'energy' ? 0.68 : kind === 'trainer' ? 0.9 : 0.88);
  const limit = opts?.limit ?? 8;
  const effects = await loadServerEffects();
  const ranked = effects
    .filter(effect => !kind || effect.kind === kind || (!effect.kind && kind === 'attack'))
    .map(effect => ({
      effect,
      score: scoreEffectTexts(text, effect.effectText || effect.attackText || ''),
    }))
    .filter(({ score }) => score >= minScore)
    .sort((a, b) => b.score - a.score);

  const seen = new Set<string>();
  const out: ServerEffect[] = [];
  for (const { effect, score } of ranked) {
    const key = `${effect.kind}:${normalizeEffectCorpus(effect.effectText || '')}:${(effect.body || []).join('|')}`;
    if (seen.has(key)) continue;
    seen.add(key);
    out.push({ ...effect, similarity: score });
    if (out.length >= limit) break;
  }
  return out;
}

export async function findServerEffect(text: string, kind?: EffectKind): Promise<ServerEffect | undefined> {
  const [best] = await findServerEffects(text, kind);
  return best;
}

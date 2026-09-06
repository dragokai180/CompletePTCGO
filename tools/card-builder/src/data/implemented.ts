/** Loads implemented-card ids (EN catalog) and Spirit-script index for Japan matching. */

import { identityName } from '../generator/pokemonReprintIdentity';

let cachedIds: Set<string> | null = null;
let cachedJp: ImplementedJpIndex | null = null;

export interface ImplementedJpIndex {
  namesBySet: Record<string, string[]>;
  pokemonIdentitiesBySet: Record<string, string[]>;
}

export async function loadImplementedCardIds(): Promise<Set<string>> {
  if (cachedIds) return cachedIds;
  try {
    const res = await fetch('/implemented-card-ids.json');
    if (!res.ok) {
      console.warn('implementedCardIds.json not found — browse will not grey out unimplemented cards.');
      cachedIds = new Set();
      return cachedIds;
    }
    const data = (await res.json()) as { implementedCardIds?: string[] };
    cachedIds = new Set(data.implementedCardIds || []);
  } catch (e) {
    console.warn('Failed to load implemented card ids', e);
    cachedIds = new Set();
  }
  return cachedIds;
}

export async function loadImplementedJpIndex(): Promise<ImplementedJpIndex> {
  if (cachedJp) return cachedJp;
  try {
    const res = await fetch('/implemented-jp.json');
    if (!res.ok) {
      cachedJp = { namesBySet: {}, pokemonIdentitiesBySet: {} };
      return cachedJp;
    }
    cachedJp = (await res.json()) as ImplementedJpIndex;
  } catch (e) {
    console.warn('Failed to load Japanese implemented index', e);
    cachedJp = { namesBySet: {}, pokemonIdentitiesBySet: {} };
  }
  return cachedJp;
}

export function clearImplementedCache(): void {
  cachedIds = null;
  cachedJp = null;
}

export function isImplemented(ids: Set<string>, cardId: string): boolean {
  return ids.has(cardId);
}

export function isImplementedJp(
  index: ImplementedJpIndex | null | undefined,
  card: {
    name: string;
    category?: string;
    spiritSet?: string;
    reprintIdentity?: string;
  }
): boolean {
  if (!index) return false;
  const set = String(card.spiritSet || '').toUpperCase();
  if (!set) return false;
  const category = (card.category || '').toLowerCase();
  const names = index.namesBySet[set] || [];
  const nameHit = names.includes(identityName(card.name));
  if (category === 'pokemon') {
    const identities = index.pokemonIdentitiesBySet[set] || [];
    if (card.reprintIdentity && identities.includes(card.reprintIdentity)) return true;
    return nameHit;
  }
  return nameHit;
}

export function implementedJpCount(index: ImplementedJpIndex | null | undefined): number {
  if (!index) return 0;
  let n = 0;
  for (const names of Object.values(index.namesBySet)) n += names.length;
  return n;
}

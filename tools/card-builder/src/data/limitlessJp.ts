import type {
  TcgDexCard,
  TcgDexCardResume,
  TcgDexSerieResume,
  TcgDexSet,
  TcgDexSetResume,
} from './types';
import { DataError } from './types';
import { mapTcgDexCardToDraft } from '../tcgdex/mapCardToDraft';
import { pokemonReprintIdentityFromDraft } from '../generator/pokemonReprintIdentity';
import { spiritSetCodeFromJpSet } from '../generator/setMapping';

const DATA_BASE = '/limitless-jp';

export interface JpSetIndex {
  series: Array<{ id: string; name: string; logo?: string }>;
  sets: Array<{
    id: string;
    name: string;
    series: string;
    seriesName?: string;
    logo?: string;
    releaseDate?: string;
    cardCount?: number;
  }>;
}

export interface JpSetPayload {
  set: JpSetIndex['sets'][number];
  cards: TcgDexCard[];
}

let cachedIndex: JpSetIndex | null = null;
const cardCache = new Map<string, JpSetPayload>();

async function getJson<T>(path: string): Promise<T> {
  let res: Response;
  try {
    res = await fetch(`${DATA_BASE}${path}`);
  } catch (e) {
    throw new DataError(
      `Limitless JP catalog unreachable (${e instanceof Error ? e.message : String(e)}). Run: npm run sync-data:jp`
    );
  }
  if (!res.ok) {
    const body = await res.text().catch(() => '');
    let detail = '';
    try {
      detail = JSON.parse(body).error || '';
    } catch {
      detail = body.slice(0, 180);
    }
    throw new DataError(
      detail || `Failed to load Japanese catalog ${path} (${res.status})`,
      res.status
    );
  }
  return (await res.json()) as T;
}

async function loadIndex(): Promise<JpSetIndex> {
  if (cachedIndex) return cachedIndex;
  cachedIndex = await getJson<JpSetIndex>('/sets.json');
  return cachedIndex;
}

async function loadSetPayload(setId: string): Promise<JpSetPayload> {
  const hit = cardCache.get(setId);
  if (hit) return hit;
  const payload = await getJson<JpSetPayload>(`/cards/${encodeURIComponent(setId)}.json`);
  cardCache.set(setId, payload);
  return payload;
}

function toSetResume(s: JpSetIndex['sets'][number]): TcgDexSetResume {
  return {
    id: s.id,
    name: s.name,
    logo: s.logo,
    cardCount: { total: s.cardCount ?? 0, official: s.cardCount ?? 0 },
  };
}

function enrichResume(card: TcgDexCard): TcgDexCardResume {
  const spiritSet = spiritSetCodeFromJpSet(card.set?.id || '');
  let reprintIdentity: string | undefined;
  if ((card.category || '').toLowerCase() === 'pokemon') {
    try {
      reprintIdentity = pokemonReprintIdentityFromDraft(mapTcgDexCardToDraft(card));
    } catch {
      reprintIdentity = undefined;
    }
  }
  return {
    id: card.id,
    localId: card.localId,
    name: card.name,
    image: card.image,
    category: card.category,
    spiritSet,
    reprintIdentity,
  };
}

export async function listSeries(): Promise<TcgDexSerieResume[]> {
  const index = await loadIndex();
  return index.series.map(s => ({
    id: s.id,
    name: `${s.name} (${index.sets.filter(x => x.series === s.id).length})`,
    logo: s.logo,
  }));
}

export async function getSerie(serieId: string): Promise<{
  id: string;
  name: string;
  sets: TcgDexSetResume[];
}> {
  const index = await loadIndex();
  const matched = index.sets.filter(s => s.series === serieId);
  const serie = index.series.find(s => s.id === serieId);
  return {
    id: serieId,
    name: serie?.name || serieId,
    sets: matched.map(toSetResume),
  };
}

export async function getSet(setId: string): Promise<TcgDexSet> {
  const payload = await loadSetPayload(setId);
  const set = payload.set;
  return {
    id: set.id,
    name: set.name,
    logo: set.logo,
    cardCount: { total: set.cardCount ?? payload.cards.length, official: set.cardCount ?? payload.cards.length },
    serie: { id: set.series, name: set.seriesName || set.series },
    tcgOnline: set.id,
    releaseDate: set.releaseDate || '',
    cards: payload.cards.map(enrichResume),
  };
}

export async function getCard(id: string): Promise<TcgDexCard> {
  const m = String(id || '').match(/^jp-([A-Za-z0-9]+)-(.+)$/);
  if (!m) throw new DataError(`Invalid Japanese catalog id: ${id}`);
  const payload = await loadSetPayload(m[1]);
  const card = payload.cards.find(c => c.id === id);
  if (!card) throw new DataError(`Card not found: ${id}`, 404);
  return card;
}

export async function searchCardsByName(name: string): Promise<TcgDexCardResume[]> {
  const q = name.trim();
  if (!q) return [];
  const cards = await getJson<TcgDexCard[]>(`/search?q=${encodeURIComponent(q)}`);
  return cards.map(enrichResume);
}

export function clearJpCache(): void {
  cachedIndex = null;
  cardCache.clear();
}

export const JP_SOURCE_NOTE =
  'Japan tab uses Limitless TCG unofficial English translations (cached locally). Prefab matching may miss if wording differs from official EN text.';

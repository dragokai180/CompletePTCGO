/**
 * Fetch + parse Limitless Japanese card pages (unofficial English translations).
 * Shared by sync-limitless-jp.mjs and the Vite card-builder middleware.
 */
import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { get as httpsGet } from 'node:https';
import { get as httpGet } from 'node:http';
import { spiritSetCodeFromJpSet } from './jp-set-mapping.mjs';

export const LIMITLESS_ORIGIN = 'https://limitlesstcg.com';
export const USER_AGENT = 'SpiritCardBuilder/1.0 (local card-builder; +https://github.com)';

const LETTER_TO_TYPE = {
  G: 'Grass',
  R: 'Fire',
  W: 'Water',
  L: 'Lightning',
  P: 'Psychic',
  F: 'Fighting',
  D: 'Darkness',
  M: 'Metal',
  Y: 'Fairy',
  N: 'Dragon',
  C: 'Colorless',
};

const TYPE_NAME = {
  grass: 'Grass',
  fire: 'Fire',
  water: 'Water',
  lightning: 'Lightning',
  electric: 'Lightning',
  psychic: 'Psychic',
  fighting: 'Fighting',
  darkness: 'Darkness',
  dark: 'Darkness',
  metal: 'Metal',
  steel: 'Metal',
  fairy: 'Fairy',
  dragon: 'Dragon',
  colorless: 'Colorless',
};

const MONTHS = {
  jan: '01',
  feb: '02',
  mar: '03',
  apr: '04',
  may: '05',
  jun: '06',
  jul: '07',
  aug: '08',
  sep: '09',
  oct: '10',
  nov: '11',
  dec: '12',
};

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

export function decodeHtml(s) {
  return String(s || '')
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"')
    .replace(/&#39;|&apos;/g, "'")
    .replace(/&nbsp;/g, ' ')
    .replace(/&#(\d+);/g, (_, n) => String.fromCharCode(Number(n)))
    .replace(/&#x([0-9a-f]+);/gi, (_, n) => String.fromCharCode(parseInt(n, 16)));
}

export function stripTags(html) {
  return decodeHtml(String(html || '').replace(/<[^>]+>/g, ' '))
    .replace(/\[\s+([GRWLPFDMYNC])\s+\]/gi, '[$1]')
    .replace(/\s+/g, ' ')
    .trim();
}

function inner(html, openRe) {
  const m = String(html || '').match(openRe);
  return m ? m[1] : '';
}

function normalizeTypeName(raw) {
  const key = String(raw || '')
    .trim()
    .toLowerCase();
  if (!key || key === 'none') return '';
  return TYPE_NAME[key] || String(raw).trim();
}

function costFromSymbols(symbols) {
  const letters = String(symbols || '')
    .toUpperCase()
    .replace(/[^GRWLPFDMYNC]/g, '');
  return [...letters].map(l => LETTER_TO_TYPE[l] || 'Colorless');
}

function parseAttackInfo(infoHtml) {
  const symbols = inner(infoHtml, /<span class="ptcg-symbol">([\s\S]*?)<\/span>/i);
  const rest = stripTags(infoHtml.replace(/<span class="ptcg-symbol">[\s\S]*?<\/span>/gi, ' '));
  const dmg = rest.match(/\s(\d+[+x×\-]?)\s*$/i);
  const name = dmg ? rest.slice(0, dmg.index).trim() : rest;
  return {
    cost: costFromSymbols(stripTags(symbols) || symbols),
    name,
    damage: dmg ? dmg[1].replace('×', 'x') : undefined,
  };
}

function parseAbilityInfo(infoText) {
  const t = infoText.trim();
  const m = t.match(/^(Ability|Pok[ée]-Power|Pok[ée]-Body|Pokémon Power|Pokemon Power|Ancient Trait)\s*:\s*(.*)$/i);
  if (m) return { type: m[1].replace(/é/g, 'e'), name: m[2].trim() };
  return { type: 'Ability', name: t };
}

function parseWrr(text) {
  const weaknesses = [];
  const resistances = [];
  let retreat = 0;
  const weak = text.match(/Weakness:\s*([A-Za-z]+)/i);
  const res = text.match(/Resistance:\s*([A-Za-z]+)(?:\s*([+\-]?\d+))?/i);
  const ret = text.match(/Retreat:\s*(\d+)/i);
  const weakType = normalizeTypeName(weak?.[1]);
  if (weakType) weaknesses.push({ type: weakType, value: '×2' });
  const resType = normalizeTypeName(res?.[1]);
  if (resType) {
    resistances.push({ type: resType, value: res?.[2] || '-20' });
  }
  if (ret) {
    const n = parseInt(ret[1], 10);
    retreat = Number.isFinite(n) ? n : 0;
  }
  return { weaknesses, resistances, retreat };
}

function parseReleaseDate(raw) {
  const t = stripTags(raw);
  const m = t.match(/^(\d{1,2})\s+([A-Za-z]{3})\s+(\d{2})$/);
  if (!m) return t;
  const month = MONTHS[m[2].toLowerCase()];
  if (!month) return t;
  const year = Number(m[3]) >= 70 ? `19${m[3]}` : `20${m[3]}`;
  return `${year}-${month}-${m[1].padStart(2, '0')}`;
}

export function parseSetsIndex(html) {
  const table = inner(html, /<table class="[^"]*sets-table[^"]*"[\s\S]*?>([\s\S]*?)<\/table>/i);
  const series = [];
  const sets = [];
  let currentSerie = { id: 'other', name: 'Other' };
  const rowRe = /<tr\b[^>]*>([\s\S]*?)<\/tr>/gi;
  let row;
  while ((row = rowRe.exec(table))) {
    const body = row[1];
    const heading = inner(body, /<th class="sub-heading"[^>]*>([\s\S]*?)<\/th>/i);
    if (heading) {
      const name = stripTags(heading);
      currentSerie = { id: name, name };
      if (!series.some(s => s.id === currentSerie.id)) series.push(currentSerie);
      continue;
    }
    const href = inner(body, /href="\/cards\/jp\/([^"/?#]+)"/i);
    if (!href) continue;
    const nameHtml = inner(body, /<a href="\/cards\/jp\/[^"]+"[\s\S]*?>([\s\S]*?)<\/a>/i);
    const name = stripTags(nameHtml.replace(/<span class="code[\s\S]*?<\/span>/gi, ' '));
    const logo = inner(body, /<img class="set"[^>]*src="([^"]+)"/i);
    const cells = [...body.matchAll(/<td\b[^>]*>([\s\S]*?)<\/td>/gi)].map(m => m[1]);
    const dateCell = cells[1] || '';
    const count = inner(cells[2] || '', />([\d,]+)/);
    const set = {
      id: href,
      name: name || href,
      series: currentSerie.id,
      seriesName: currentSerie.name,
      logo: logo || `https://s3.limitlesstcg.com/sets/jp/${href}.png`,
      releaseDate: parseReleaseDate(dateCell),
      cardCount: Number(String(count || '').replace(/,/g, '')) || 0,
    };
    sets.push(set);
    if (!currentSerie.logo && set.logo) currentSerie.logo = set.logo;
  }
  for (const s of series) {
    const first = sets.find(x => x.series === s.id);
    if (first?.logo) s.logo = first.logo;
  }
  return { series, sets };
}

function parseIntPrints(block) {
  const table = inner(block, /<table class="card-prints-versions">([\s\S]*?)<\/table>/i);
  if (!table) return [];
  const jpIdx = table.search(/JP\. Prints/i);
  const intPart = jpIdx >= 0 ? table.slice(0, jpIdx) : table;
  const out = [];
  const re = /<a[^>]*href="\/cards\/en\/([^"/]+)\/([^"]+)"[^>]*>([\s\S]*?)<\/a>/gi;
  let m;
  while ((m = re.exec(intPart))) {
    const setName = stripTags(m[3].replace(/<span[\s\S]*?<\/span>/gi, ' '));
    const number = stripTags(inner(m[3], /prints-table-card-number[^"]*">([\s\S]*?)<\/span>/i)).replace(
      /^#/,
      ''
    );
    out.push({
      set: m[1],
      number: number || m[2],
      setName,
    });
  }
  return out;
}

function parseCardProfile(block, fallbackSetId) {
  const nameHref = inner(block, /<span class="card-text-name">[\s\S]*?<a href="([^"]+)"/i);
  const name = stripTags(inner(block, /<span class="card-text-name">[\s\S]*?<a[^>]*>([\s\S]*?)<\/a>/i));
  const path = decodeHtml(nameHref);
  const idMatch = path.match(/\/cards\/jp\/([^/?#]+)\/([^/?#]+)/i);
  const setId = idMatch?.[1] || fallbackSetId;
  const localId = idMatch?.[2] || '';
  const imgLg = inner(block, /<div class="card-image">[\s\S]*?src="([^"]+)"/i);
  const imgHi = inner(block, /data-src="([^"]+)"/i) || imgLg.replace(/_LG\.png/i, '.png');

  const titleLine = stripTags(inner(block, /<p class="card-text-title">([\s\S]*?)<\/p>/i));
  const typeLine = stripTags(inner(block, /<p class="card-text-type">([\s\S]*?)<\/p>/i));
  const hpMatch = titleLine.match(/-\s*(\d+)\s*HP\b/i);
  const typeMatch = titleLine.match(/-\s*([A-Za-z]+)\s*-\s*\d+\s*HP/i);

  const kind = (typeLine.split('-')[0] || '').trim().toLowerCase();
  let category = 'Pokemon';
  if (kind.startsWith('trainer')) category = 'Trainer';
  else if (kind.startsWith('energy')) category = 'Energy';

  let stage;
  let evolveFrom;
  let trainerType;
  let energyType;
  let suffix;
  if (category === 'Pokemon') {
    const stageMatch = typeLine.match(/-\s*(Basic|Stage\s*1|Stage\s*2|VMAX|VSTAR|V-UNION|VUNION|MEGA|BREAK|Restored|Level-Up|LEGEND)\b/i);
    stage = stageMatch ? stageMatch[1].replace(/\s+/g, '') : 'Basic';
    if (/^stage1$/i.test(stage)) stage = 'Stage1';
    if (/^stage2$/i.test(stage)) stage = 'Stage2';
    const evo = typeLine.match(/Evolves from\s+(.+)$/i);
    evolveFrom = evo ? evo[1].trim() : undefined;
    if (/\bex\b/i.test(name)) suffix = 'ex';
    else if (/\bGX\b/i.test(name)) suffix = 'GX';
    else if (/\bVMAX\b/i.test(name)) suffix = 'VMAX';
    else if (/\bVSTAR\b/i.test(name)) suffix = 'VSTAR';
    else if (/(^|\s)V$/i.test(name)) suffix = 'V';
  } else if (category === 'Trainer') {
    const t = typeLine.match(/-\s*(Item|Supporter|Stadium|Tool|Pokémon Tool|Pokemon Tool)\b/i);
    trainerType = t ? t[1].replace(/Pokémon Tool|Pokemon Tool/i, 'Tool') : 'Item';
  } else {
    energyType = /special/i.test(typeLine) ? 'Special' : 'Basic';
  }

  const attacks = [];
  const abilities = [];
  const attackRe = /<div class="card-text-attack">([\s\S]*?)<\/div>/gi;
  let am;
  while ((am = attackRe.exec(block))) {
    const info = parseAttackInfo(inner(am[1], /<p class="card-text-attack-info">([\s\S]*?)<\/p>/i));
    const effect = stripTags(inner(am[1], /<p class="card-text-attack-effect">([\s\S]*?)<\/p>/i));
    attacks.push({
      cost: info.cost,
      name: info.name,
      damage: info.damage,
      effect: effect || undefined,
    });
  }
  const abilityRe = /<div class="card-text-ability">([\s\S]*?)<\/div>/gi;
  while ((am = abilityRe.exec(block))) {
    const info = parseAbilityInfo(stripTags(inner(am[1], /<p class="card-text-ability-info">([\s\S]*?)<\/p>/i)));
    const effect = stripTags(inner(am[1], /<p class="card-text-ability-effect">([\s\S]*?)<\/p>/i));
    abilities.push({ type: info.type, name: info.name, effect });
  }

  let effect;
  if (category !== 'Pokemon') {
    const sections = [...block.matchAll(/<div class="card-text-section">([\s\S]*?)<\/div>/gi)].map(x => x[1]);
    const textSection = sections.find(
      s =>
        !/card-text-title|card-text-type|card-text-wrr|card-text-artist|card-text-attack|card-text-ability/i.test(s) &&
        stripTags(s)
    );
    effect = textSection ? stripTags(textSection) : undefined;
  }

  const wrr = parseWrr(stripTags(inner(block, /<p class="card-text-wrr">([\s\S]*?)<\/p>/i)));
  const illustrator = stripTags(inner(block, /<div class="card-text-section card-text-artist">[\s\S]*?<a[^>]*>([\s\S]*?)<\/a>/i));
  const reg = stripTags(inner(block, /<div class="regulation-mark">([\s\S]*?)<\/div>/i));
  const regulationMark = (reg.match(/^([A-Z])\s+Regulation Mark/i) || [])[1] || '';
  const printDetails = stripTags(inner(block, /<div class="prints-current-details">([\s\S]*?)<\/div>/i));
  const rarity = (printDetails.match(/·\s*(.+)$/) || [])[1] || '';
  const intPrints = parseIntPrints(block);

  return {
    id: `jp-${setId}-${localId}`,
    localId,
    name,
    image: imgHi || imgLg,
    category,
    illustrator: illustrator || undefined,
    rarity,
    hp: hpMatch ? Number(hpMatch[1]) : undefined,
    types: typeMatch ? [normalizeTypeName(typeMatch[1])].filter(Boolean) : undefined,
    evolveFrom,
    stage,
    suffix,
    abilities: abilities.length ? abilities : undefined,
    attacks: attacks.length ? attacks : undefined,
    weaknesses: wrr.weaknesses.length ? wrr.weaknesses : undefined,
    resistances: wrr.resistances.length ? wrr.resistances : undefined,
    retreat: category === 'Pokemon' ? wrr.retreat : undefined,
    effect,
    trainerType,
    energyType,
    regulationMark: regulationMark || undefined,
    intPrints: intPrints.length ? intPrints : undefined,
    setId,
  };
}

export function parseSetCards(html, setMeta) {
  const blocks = html.split(/<div class="card-profile">/i).slice(1);
  const cards = [];
  const seen = new Set();
  for (const chunk of blocks) {
    const block = `<div class="card-profile">${chunk}`;
    try {
      const card = parseCardProfile(block, setMeta.id);
      if (!card.name || !card.localId || seen.has(card.id)) continue;
      seen.add(card.id);
      card.set = {
        id: setMeta.id,
        name: setMeta.name,
        logo: setMeta.logo,
        cardCount: { total: setMeta.cardCount || 0, official: setMeta.cardCount || 0 },
        abbreviations: { official: setMeta.id },
        tcgOnline: setMeta.id,
      };
      cards.push(card);
    } catch {
      /* skip malformed card block */
    }
  }
  return cards;
}

function fetchUrl(url) {
  return new Promise((resolve, reject) => {
    const getter = url.startsWith('https') ? httpsGet : httpGet;
    const req = getter(
      url,
      {
        headers: {
          'User-Agent': USER_AGENT,
          Accept: 'text/html,application/xhtml+xml',
        },
      },
      res => {
        if (res.statusCode && res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
          const next = new URL(res.headers.location, url).toString();
          fetchUrl(next).then(resolve, reject);
          return;
        }
        if (res.statusCode !== 200) {
          reject(new Error(`HTTP ${res.statusCode} for ${url}`));
          return;
        }
        const chunks = [];
        res.on('data', c => chunks.push(c));
        res.on('end', () => resolve(Buffer.concat(chunks).toString('utf8')));
      }
    );
    req.on('error', reject);
  });
}

export async function fetchLimitless(pathAndQuery) {
  const url = pathAndQuery.startsWith('http') ? pathAndQuery : `${LIMITLESS_ORIGIN}${pathAndQuery}`;
  return fetchUrl(url);
}

export function cachePaths(cacheDir) {
  return {
    sets: join(cacheDir, 'sets.json'),
    cardsDir: join(cacheDir, 'cards'),
    cardFile(setId) {
      return join(cacheDir, 'cards', `${setId}.json`);
    },
  };
}

const inflight = new Map();

function once(key, fn) {
  const hit = inflight.get(key);
  if (hit) return hit;
  const p = fn().finally(() => inflight.delete(key));
  inflight.set(key, p);
  return p;
}

export async function loadOrFetchSets(cacheDir, { force = false } = {}) {
  const paths = cachePaths(cacheDir);
  if (!force && existsSync(paths.sets)) {
    return JSON.parse(readFileSync(paths.sets, 'utf8'));
  }
  return once('sets', async () => {
    const html = await fetchLimitless('/cards/jp');
    const parsed = parseSetsIndex(html);
    mkdirSync(cacheDir, { recursive: true });
    writeFileSync(paths.sets, JSON.stringify(parsed, null, 2));
    return parsed;
  });
}

export async function loadOrFetchSetCards(cacheDir, setId, { force = false, delayMs = 0 } = {}) {
  const paths = cachePaths(cacheDir);
  const file = paths.cardFile(setId);
  if (!force && existsSync(file)) {
    return JSON.parse(readFileSync(file, 'utf8'));
  }
  return once(`set:${setId}`, async () => {
    if (delayMs) await sleep(delayMs);
    const index = await loadOrFetchSets(cacheDir);
    const setMeta = index.sets.find(s => s.id === setId);
    if (!setMeta) throw new Error(`Unknown Japanese set: ${setId}`);
    const html = await fetchLimitless(
      `/cards/jp/${encodeURIComponent(setId)}?translate=en&display=full&show=all`
    );
    const cards = parseSetCards(html, setMeta);
    mkdirSync(dirname(file), { recursive: true });
    const payload = { set: setMeta, cards };
    writeFileSync(file, JSON.stringify(payload));
    return payload;
  });
}

export async function searchLimitlessCards(cacheDir, query) {
  const q = String(query || '').trim();
  if (!q) return [];
  const html = await fetchLimitless(
    `/cards/jp?q=${encodeURIComponent(q)}&translate=en&display=full&show=all`
  );
  const index = await loadOrFetchSets(cacheDir);
  const fallback = { id: 'search', name: 'Search', cardCount: 0, logo: '' };
  const cards = parseSetCards(html, fallback);
  for (const card of cards) {
    const meta = index.sets.find(s => s.id === card.setId) || fallback;
    card.set = {
      id: card.setId || meta.id,
      name: meta.name || card.setId,
      logo: meta.logo,
      cardCount: { total: meta.cardCount || 0, official: meta.cardCount || 0 },
      abbreviations: { official: card.setId || meta.id },
      tcgOnline: card.setId || meta.id,
    };
  }
  return cards.slice(0, 80);
}

export function jpSpiritSet(setId) {
  return spiritSetCodeFromJpSet(setId);
}

/** Spirit set folder ↔ pokemon-tcg-data set id (browser copy of scripts/set-mapping.mjs). */

export const JP_TO_SPIRIT: Record<string, string> = {
  M1: 'ME1',
  M1L: 'ME1',
  M1S: 'ME1',
  M2: 'ME2',
  M2a: 'ME2PT5',
  M3: 'ME3',
  M4: 'ME4',
  M5: 'ME5',
  SV6a: 'SV065',
  SV8a: 'SV085',
};

export function spiritSetCodeFromJpSet(jpSet: string): string {
  const raw = String(jpSet || '').trim();
  if (!raw) return '';
  if (JP_TO_SPIRIT[raw]) return JP_TO_SPIRIT[raw];
  const upper = raw.toUpperCase();
  if (JP_TO_SPIRIT[upper]) return JP_TO_SPIRIT[upper];
  const mega = raw.match(/^M(\d+)$/i);
  if (mega) return `ME${mega[1]}`;
  const sv = raw.match(/^SV(\d+)$/i);
  if (sv) return `SV${String(Number(sv[1])).padStart(2, '0')}`;
  const sva = raw.match(/^SV(\d+)a$/i);
  if (sva) return `SV${String(Number(sva[1])).padStart(2, '0')}5`;
  return upper;
}

export function jpCatalogParts(catalogId: string): { set: string; number: string } | null {
  const m = String(catalogId || '').match(/^jp-([A-Za-z0-9]+)-(.+)$/);
  if (!m) return null;
  return { set: m[1], number: m[2] };
}

export const SPIRIT_TO_TCG_SET_IDS: Record<string, string[]> = {
  SWSH1: ['swsh1'],
  SWSH2: ['swsh2'],
  SWSH3: ['swsh3'],
  SWSH35: ['swsh35'],
  SWSH4: ['swsh4'],
  SWSH45: ['swsh45', 'swsh45sv'],
  SWSH5: ['swsh5'],
  SWSH6: ['swsh6'],
  SWSH7: ['swsh7'],
  SWSH8: ['swsh8'],
  SWSH9: ['swsh9'],
  SWSH10: ['swsh10', 'swsh10tg'],
  SWSH11: ['swsh11', 'swsh11tg'],
  SWSH12: ['swsh12', 'swsh12tg'],
  CZ: ['swsh12pt5', 'swsh12pt5gg'],
  PGO: ['pgo'],
  CEL25: ['cel25', 'cel25c'],
  SV1: ['sv1'],
  SV01: ['sv1'],
  SV02: ['sv2'],
  SV03: ['sv3'],
  SV04: ['sv4'],
  SV05: ['sv5'],
  SV06: ['sv6'],
  SV065: ['sv6pt5'],
  SV07: ['sv7'],
  SV08: ['sv8'],
  SV085: ['sv8pt5'],
  SV09: ['sv9'],
  SV10: ['sv10'],
  BASE1: ['base1'],
  BW1: ['bw1'],
};

const TCG_TO_SPIRIT: Record<string, string> = (() => {
  const map: Record<string, string> = {};
  for (const [spirit, ids] of Object.entries(SPIRIT_TO_TCG_SET_IDS)) {
    for (const id of ids) {
      if (!map[id]) map[id] = spirit;
    }
  }
  return map;
})();

export function spiritSetCodeFromCatalogId(catalogId: string): string {
  const jp = jpCatalogParts(catalogId);
  if (jp) return spiritSetCodeFromJpSet(jp.set);
  const dash = String(catalogId || '').indexOf('-');
  if (dash <= 0) return '';
  const setId = catalogId.slice(0, dash);
  if (TCG_TO_SPIRIT[setId]) return TCG_TO_SPIRIT[setId];
  const sv = setId.match(/^sv(\d+)$/i);
  if (sv) return `SV${String(Number(sv[1])).padStart(2, '0')}`;
  const svpt = setId.match(/^sv(\d+)pt5$/i);
  if (svpt) return `SV${String(Number(svpt[1])).padStart(2, '0')}5`;
  return setId.toUpperCase();
}

export function spiritSetCodeFromPtcgoOrId(setField: string, catalogId?: string): string {
  if (catalogId) {
    const fromId = spiritSetCodeFromCatalogId(catalogId);
    if (fromId) return fromId;
  }
  const upper = String(setField || '').trim().toUpperCase();
  if (SPIRIT_TO_TCG_SET_IDS[upper]) return upper;
  // Already a Spirit code like SWSH12
  if (/^(SWSH|SV|BW|SM|XY|PGO|CZ|CEL|ME)/i.test(upper)) return upper;
  // Reverse-lookup ptcgo → first spirit that maps (rare)
  return upper;
}

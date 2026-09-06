/**
 * Japanese Limitless set codes → Spirit folder codes.
 * Collector numbers often differ between JP and EN; this is set-level only.
 */

export const JP_TO_SPIRIT = {
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

export function spiritSetCodeFromJpSet(jpSet) {
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

/** Catalog ids look like jp-M3-21 or jp-M2a-10. */
export function jpCatalogParts(catalogId) {
  const m = String(catalogId || '').match(/^jp-([A-Za-z0-9]+)-(.+)$/);
  if (!m) return null;
  return { set: m[1], number: m[2] };
}

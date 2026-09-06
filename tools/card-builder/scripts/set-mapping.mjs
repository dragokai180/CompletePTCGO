/**
 * Maps between Spirit set folder codes (SV09, SWSH12, CZ, …) and
 * pokemon-tcg-data set ids / ptcgoCodes.
 */
import { jpCatalogParts, spiritSetCodeFromJpSet } from './jp-set-mapping.mjs';

export { JP_TO_SPIRIT, jpCatalogParts, spiritSetCodeFromJpSet } from './jp-set-mapping.mjs';

/** Spirit folder/code → primary pokemon-tcg-data set id (and extras for galleries). */
export const SPIRIT_TO_TCG_SET_IDS = {
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
  SV03pt5: ['sv3pt5'],
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

/** Catalog set id → Spirit folder code. */
export const TCG_SET_ID_TO_SPIRIT = (() => {
  const map = {};
  for (const [spirit, ids] of Object.entries(SPIRIT_TO_TCG_SET_IDS)) {
    for (const id of ids) {
      if (!map[id]) map[id] = spirit;
    }
  }
  return map;
})();

/**
 * Heuristic when SPIRIT_TO_TCG_SET_IDS has no entry:
 * SV05 → sv5, SWSH12 → swsh12, etc.
 */
export function heuristicCatalogIds(spiritCode) {
  const code = String(spiritCode || '').toUpperCase();
  if (!code) return [];
  if (SPIRIT_TO_TCG_SET_IDS[code]) return SPIRIT_TO_TCG_SET_IDS[code];

  const m = code.match(/^SV0*(\d+)(?:(\d))?$/i);
  if (m) {
    // SV085 → already in table; SV05 → sv5; SV9 → sv9
    const n = m[1].replace(/^0+/, '') || '0';
    if (m[2] !== undefined) {
      // e.g. weird patterns — leave empty
    }
    return [`sv${n}`];
  }
  if (/^SWSH/i.test(code)) {
    return [code.toLowerCase()];
  }
  return [code.toLowerCase()];
}

/** Resolve Spirit set code for a catalog card id like "sv9-22" or "jp-M3-21". */
export function spiritSetCodeFromCatalogId(catalogId) {
  const jp = jpCatalogParts(catalogId);
  if (jp) return spiritSetCodeFromJpSet(jp.set);
  const dash = String(catalogId || '').indexOf('-');
  if (dash <= 0) return '';
  const setId = catalogId.slice(0, dash);
  if (TCG_SET_ID_TO_SPIRIT[setId]) return TCG_SET_ID_TO_SPIRIT[setId];
  // sv5 → SV05, swsh12 → SWSH12, sv8pt5 → SV085 (fallback)
  if (/^sv(\d+)$/i.test(setId)) {
    const n = Number(RegExp.$1);
    return `SV${String(n).padStart(2, '0')}`;
  }
  if (/^sv(\d+)pt5$/i.test(setId)) {
    const n = Number(RegExp.$1);
    return `SV${String(n).padStart(2, '0')}5`;
  }
  return setId.toUpperCase();
}

export function cleanName(name) {
  return String(name || '').replace(/[^a-zA-Z0-9]/g, '');
}

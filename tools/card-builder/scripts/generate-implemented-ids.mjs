/**
 * Builds implementedCardIds.json by scanning Spirit card scripts and mapping
 * set_code + collector_number onto PokemonTCG/pokemon-tcg-data card ids.
 *
 * Usage (from tools/card-builder):
 *   npm run sync-data
 *   npm run generate:implemented-ids
 */
import { existsSync, mkdirSync, readdirSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { SPIRIT_TO_TCG_SET_IDS, heuristicCatalogIds } from './set-mapping.mjs';

const rootDir = join(dirname(fileURLToPath(import.meta.url)), '..');
const repoRoot = join(rootDir, '../..');
const scriptsRoot = join(repoRoot, 'spirit/game/scripts/cards');
const setsJsonPath = join(repoRoot, 'spirit/database/json_data/sets.json');
const dataRoot = join(rootDir, 'data/pokemon-tcg-data');
const setsFile = join(dataRoot, 'sets/en.json');
const cardsDir = join(dataRoot, 'cards/en');
const outFile = join(rootDir, 'implementedCardIds.json');

function loadLocalSets() {
  if (!existsSync(setsFile)) {
    console.error(`Missing ${setsFile}`);
    console.error('Run: npm run sync-data');
    process.exit(1);
  }
  return JSON.parse(readFileSync(setsFile, 'utf8'));
}

function buildCodeToSetIds(localSets) {
  const map = new Map();
  const sorted = [...localSets].sort((a, b) =>
    String(a.releaseDate || '').localeCompare(String(b.releaseDate || ''))
  );
  for (const s of sorted) {
    if (!s.ptcgoCode) continue;
    const list = map.get(s.ptcgoCode) || [];
    list.push(s.id);
    map.set(s.ptcgoCode, list);
  }
  return map;
}

function createCardIndex() {
  const bySet = new Map();

  function loadSet(setId) {
    if (bySet.has(setId)) return bySet.get(setId);
    const file = join(cardsDir, `${setId}.json`);
    const numberToId = new Map();
    if (existsSync(file)) {
      const cards = JSON.parse(readFileSync(file, 'utf8'));
      for (const c of cards) {
        if (c.number != null && c.id) {
          numberToId.set(String(c.number), c.id);
        }
      }
    }
    bySet.set(setId, numberToId);
    return numberToId;
  }

  return {
    resolve(setIds, setNumber) {
      if (!setIds?.length) return null;
      const num = String(setNumber);
      for (const setId of setIds) {
        const hit = loadSet(setId).get(num);
        if (hit) return { id: hit, matched: true };
      }
      return { id: `${setIds[0]}-${num}`, matched: false };
    },
  };
}

function collectPyFiles(dir) {
  if (!existsSync(dir)) return [];
  return readdirSync(dir, { withFileTypes: true }).flatMap(entry => {
    const path = join(dir, entry.name);
    if (entry.isDirectory()) {
      if (entry.name === '__pycache__' || entry.name === 'CUSTOM') return [];
      return collectPyFiles(path);
    }
    return entry.name.endsWith('.py') && entry.name !== '__init__.py' ? [path] : [];
  });
}

function parseScriptMeta(source, folderName) {
  const setCode =
    source.match(/set_code\s*=\s*["']([^"']+)["']/)?.[1] ||
    source.match(/key\s*=\s*["']([^"']+)["']/)?.[1] ||
    folderName;
  const collector =
    source.match(/collector_number\s*=\s*(\d+)/)?.[1] ||
    // reprint stubs: reprint(..., collector_number=203, ...)
    source.match(/collector_number\s*=\s*(\d+)/)?.[1] ||
    source.match(/_(\d+)\.py$/)?.[1];
  // Filename fallback for number
  return { setCode: String(setCode || folderName).toUpperCase(), collector };
}

function resolveSetIds(spiritCode, ptcgoBySpirit, codeToSetIds) {
  const direct = SPIRIT_TO_TCG_SET_IDS[spiritCode] || heuristicCatalogIds(spiritCode);
  if (direct.length) return direct;
  const ptcgo = ptcgoBySpirit.get(spiritCode);
  if (ptcgo && codeToSetIds.get(ptcgo)?.length) return codeToSetIds.get(ptcgo);
  return [];
}

function main() {
  const localSets = loadLocalSets();
  const codeToSetIds = buildCodeToSetIds(localSets);
  const index = createCardIndex();

  const ptcgoBySpirit = new Map();
  if (existsSync(setsJsonPath)) {
    const spiritSets = JSON.parse(readFileSync(setsJsonPath, 'utf8'));
    for (const s of spiritSets) {
      if (s.name && s.externalId) ptcgoBySpirit.set(String(s.name).toUpperCase(), s.externalId);
    }
  }

  const files = collectPyFiles(scriptsRoot);
  const rawIds = [];
  let skippedNoCode = 0;
  let unmatchedFallback = 0;
  let skippedParse = 0;

  for (const file of files) {
    const parts = file.split(/[/\\]/);
    const folderName = parts[parts.length - 2] || '';
    const fileName = parts[parts.length - 1] || '';
    const source = readFileSync(file, 'utf8');
    let { setCode, collector } = parseScriptMeta(source, folderName);
    if (!collector) {
      const fromName = fileName.match(/_(\d+)\.py$/);
      collector = fromName?.[1];
    }
    if (!setCode || !collector) {
      skippedParse += 1;
      continue;
    }

    const setIds = resolveSetIds(setCode, ptcgoBySpirit, codeToSetIds);
    if (!setIds.length) {
      skippedNoCode += 1;
      continue;
    }
    const resolved = index.resolve(setIds, collector);
    if (!resolved) {
      skippedNoCode += 1;
      continue;
    }
    if (!resolved.matched) unmatchedFallback += 1;
    rawIds.push(resolved.id);
  }

  const seen = new Set();
  const implementedCardIds = [];
  for (const id of rawIds) {
    if (seen.has(id)) continue;
    seen.add(id);
    implementedCardIds.push(id);
  }

  writeFileSync(outFile, JSON.stringify({ implementedCardIds }, null, 2));
  console.log(`Wrote ${outFile}`);
  console.log(`  scanned ${files.length} scripts`);
  console.log(`  ${implementedCardIds.length} unique card IDs (${rawIds.length} raw)`);
  console.log(`  skipped (no set mapping): ${skippedNoCode}`);
  console.log(`  skipped (parse): ${skippedParse}`);
  console.log(`  fallback (number not in set JSON): ${unmatchedFallback}`);
}

main();

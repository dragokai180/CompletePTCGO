#!/usr/bin/env node
/**
 * Fetches Limitless Japanese set index (and optionally set card pages) into
 * data/limitless-jp. Card pages are also fetched on demand by the Vite server.
 *
 * Usage:
 *   npm run sync-data:jp              # index only
 *   npm run sync-data:jp -- --series Mega
 *   npm run sync-data:jp -- --sets M3,M6
 *   npm run sync-data:jp -- --all
 */
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { loadOrFetchSetCards, loadOrFetchSets } from './limitless-jp.mjs';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const cacheDir = join(root, 'data', 'limitless-jp');

function parseArgs(argv) {
  const out = { all: false, series: [], sets: [], force: false };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === '--all') out.all = true;
    else if (a === '--force') out.force = true;
    else if (a === '--series') out.series.push(...String(argv[++i] || '').split(',').map(s => s.trim()).filter(Boolean));
    else if (a === '--sets') out.sets.push(...String(argv[++i] || '').split(',').map(s => s.trim()).filter(Boolean));
  }
  return out;
}

const args = parseArgs(process.argv.slice(2));

console.log('Fetching Limitless Japanese set index…');
const index = await loadOrFetchSets(cacheDir, { force: args.force });
console.log(`  ${index.series.length} series, ${index.sets.length} sets`);

const wanted = new Set(args.sets);
if (args.all) {
  for (const s of index.sets) wanted.add(s.id);
} else if (args.series.length) {
  const names = new Set(args.series.map(s => s.toLowerCase()));
  for (const s of index.sets) {
    if (names.has(String(s.series).toLowerCase()) || names.has(String(s.seriesName).toLowerCase())) {
      wanted.add(s.id);
    }
  }
}

if (wanted.size === 0) {
  console.log('Index cached. Open a set in the Japan tab to fetch cards, or pass --series Mega / --sets M3,M6 / --all.');
  process.exit(0);
}

let i = 0;
for (const setId of wanted) {
  i += 1;
  process.stdout.write(`  [${i}/${wanted.size}] ${setId}… `);
  try {
    const payload = await loadOrFetchSetCards(cacheDir, setId, { force: args.force, delayMs: 450 });
    console.log(`${payload.cards.length} cards`);
  } catch (e) {
    console.log(`failed (${e instanceof Error ? e.message : e})`);
  }
}

console.log('Ready:', cacheDir);

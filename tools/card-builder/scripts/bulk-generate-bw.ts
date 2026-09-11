import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { basename, join, resolve } from 'node:path';

import { generateCardSource, scriptFileName } from '../src/generator/generateSpiritCard';
import { localCardToDraftShape, type LocalCard, type LocalSet } from '../src/data/localData';
import { mapTcgDexCardToDraft } from '../src/tcgdex/mapCardToDraft';

const ROOT = resolve(import.meta.dirname, '..', '..', '..');
const DATA_ROOT = resolve(import.meta.dirname, '..', 'data', 'pokemon-tcg-data');
const CARDS_ROOT = join(ROOT, 'spirit', 'game', 'scripts', 'cards');

// Hand-written cards that existed before the bulk import.  Refreshing is also
// monotonic below: an existing script is only replaced when the newly
// generated version has fewer unimplemented effect markers.
const PRESERVE = new Set([
  'BW1/Potion_100.py',
  'BW1/Watchog_79.py',
  'BW3/SuperRod_95.py',
  'BW3/Trubbish_48.py',
  'BW9/Exeggcute_4.py',
  'BW9/LifeDew_107.py',
]);

// Recovery aid for source migrations: a semicolon-separated set of generated
// scripts may be regenerated even when that temporarily increases their marker
// count.  Normal runs leave this empty and remain strictly monotonic.
const RESTORE = new Set(
  (process.env.BW_RESTORE || '').split(';').map((value) => value.trim()).filter(Boolean),
);

const SETS: Record<string, string> = {
  bw1: 'BW1',
  bw2: 'BW2',
  bw3: 'BW3',
  bw4: 'BW4',
  bw5: 'BW5',
  bw6: 'BW6',
  dv1: 'DV',
  bw7: 'BW7',
  bw8: 'BW8',
  bw9: 'BW9',
  bw10: 'BW10',
  bw11: 'BW11',
  bwp: 'PROMO_BW',
};

const realFetch = globalThis.fetch;
globalThis.fetch = ((input: string | URL | Request, init?: RequestInit) => {
  if (typeof input === 'string' && input.startsWith('/')) {
    return realFetch(`http://127.0.0.1:5174${input}`, init);
  }
  return realFetch(input, init);
}) as typeof fetch;

function loadJson<T>(path: string): T {
  return JSON.parse(readFileSync(path, 'utf8')) as T;
}

async function main(): Promise<void> {
  const allSets = loadJson<LocalSet[]>(join(DATA_ROOT, 'sets', 'en.json'));
  let created = 0;
  let skipped = 0;
  let failed = 0;

  for (const [dataSet, spiritSet] of Object.entries(SETS)) {
    const metadata = allSets.find((set) => set.id === dataSet);
    if (!metadata) throw new Error(`Missing set metadata: ${dataSet}`);
    const cards = loadJson<LocalCard[]>(join(DATA_ROOT, 'cards', 'en', `${dataSet}.json`));
    const outputDir = join(CARDS_ROOT, spiritSet);
    mkdirSync(outputDir, { recursive: true });

    let setCreated = 0;
    let setSkipped = 0;
    let setFailed = 0;
    for (const raw of cards) {
      try {
        const draft = mapTcgDexCardToDraft(localCardToDraftShape(raw, metadata));
        draft.spiritSetCode = spiritSet;
        const outputPath = join(outputDir, scriptFileName(draft));
        const relative = `${spiritSet}/${scriptFileName(draft)}`;
        if (spiritSet === 'BW10' || PRESERVE.has(relative)) {
          skipped += 1;
          setSkipped += 1;
          continue;
        }
        const generated = await generateCardSource(draft);
        if (existsSync(outputPath) && !RESTORE.has(relative)) {
          const existing = readFileSync(outputPath, 'utf8');
          const markerCount = (source: string) =>
            (source.match(/\bunimplemented\b/g) || []).length;
          if (markerCount(generated) >= markerCount(existing)) {
            skipped += 1;
            setSkipped += 1;
            continue;
          }
        }
        writeFileSync(outputPath, generated, 'utf8');
        created += 1;
        setCreated += 1;
      } catch (error) {
        failed += 1;
        setFailed += 1;
        console.error(`${dataSet}/${raw.id}: ${error instanceof Error ? error.stack : error}`);
      }
    }
    console.log(`${spiritSet}: ${setCreated} created, ${setSkipped} preserved, ${setFailed} failed`);
  }

  console.log(`TOTAL: ${created} created, ${skipped} preserved, ${failed} failed`);
  if (failed) process.exitCode = 1;
}

void main();

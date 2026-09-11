import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { join, resolve } from 'node:path';

import { cleanCardName } from '../src/generator/uuid5';
import type { LocalCard } from '../src/data/localData';

const ROOT = resolve(import.meta.dirname, '..', '..', '..');
const DATA_ROOT = resolve(import.meta.dirname, '..', 'data', 'pokemon-tcg-data');
const ASSET_ROOT = join(ROOT, 'spirit', 'assets', 'cards');
const SETS: Record<string, string> = {
  bw1: 'BW1', bw2: 'BW2', bw3: 'BW3', bw4: 'BW4', bw5: 'BW5', bw6: 'BW6',
  dv1: 'DV', bw7: 'BW7', bw8: 'BW8', bw9: 'BW9', bw10: 'BW10', bw11: 'BW11',
  bwp: 'PROMO_BW',
};

function loadCards(setId: string): LocalCard[] {
  const path = join(DATA_ROOT, 'cards', 'en', `${setId}.json`);
  return JSON.parse(readFileSync(path, 'utf8')) as LocalCard[];
}

async function download(card: LocalCard, folder: string): Promise<'created' | 'skipped' | 'failed'> {
  const number = String(card.number || '0').replace(/^0+(?=\d)/, '') || '0';
  const path = join(folder, `${cleanCardName(card.name)}_${number}.png`);
  if (existsSync(path)) return 'skipped';
  const url = card.images?.large || card.images?.small;
  if (!url) return 'failed';
  try {
    const response = await fetch(url);
    if (!response.ok) throw new Error(`${response.status} ${response.statusText}`);
    writeFileSync(path, Buffer.from(await response.arrayBuffer()));
    return 'created';
  } catch (error) {
    console.error(`${card.id}: ${url}: ${error instanceof Error ? error.message : error}`);
    return 'failed';
  }
}

async function main(): Promise<void> {
  let created = 0;
  let skipped = 0;
  let failed = 0;
  for (const [setId, spiritSet] of Object.entries(SETS)) {
    const folder = join(ASSET_ROOT, spiritSet);
    mkdirSync(folder, { recursive: true });
    const cards = loadCards(setId);
    let cursor = 0;
    const workers = Array.from({ length: 10 }, async () => {
      while (cursor < cards.length) {
        const card = cards[cursor++];
        const result = await download(card, folder);
        if (result === 'created') created += 1;
        else if (result === 'skipped') skipped += 1;
        else failed += 1;
      }
    });
    await Promise.all(workers);
    console.log(`${spiritSet}: ${cards.length} images checked`);
  }
  console.log(`TOTAL: ${created} downloaded, ${skipped} preserved, ${failed} failed`);
  if (failed) process.exitCode = 1;
}

void main();

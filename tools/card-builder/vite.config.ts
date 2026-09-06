import { defineConfig, type Plugin } from 'vite';
import {
  createWriteStream,
  existsSync,
  mkdirSync,
  readFileSync,
  readdirSync,
  writeFileSync,
} from 'node:fs';
import { dirname, join, relative, sep } from 'node:path';
import { fileURLToPath } from 'node:url';
import type { IncomingMessage, ServerResponse } from 'node:http';
import { get as httpsGet } from 'node:https';
import { get as httpGet } from 'node:http';
import {
  SPIRIT_TO_TCG_SET_IDS,
  jpCatalogParts,
  spiritSetCodeFromJpSet,
} from './scripts/set-mapping.mjs';
import { pokemonReprintIdentityFromScript, identityName } from './src/generator/pokemonReprintIdentity';
import {
  loadOrFetchSetCards,
  loadOrFetchSets,
  searchLimitlessCards,
} from './scripts/limitless-jp.mjs';

// local helpers (avoid TS friction with .mjs named re-exports)
function spiritSetCodeFromCatalogId(catalogId: string): string {
  const jp = jpCatalogParts(catalogId);
  if (jp) return spiritSetCodeFromJpSet(jp.set);
  const dash = String(catalogId || '').indexOf('-');
  if (dash <= 0) return '';
  const setId = catalogId.slice(0, dash);
  for (const [spirit, ids] of Object.entries(SPIRIT_TO_TCG_SET_IDS as Record<string, string[]>)) {
    if (ids.includes(setId)) return spirit;
  }
  const sv = setId.match(/^sv(\d+)$/i);
  if (sv) return `SV${String(Number(sv[1])).padStart(2, '0')}`;
  const svpt = setId.match(/^sv(\d+)pt5$/i);
  if (svpt) return `SV${String(Number(svpt[1])).padStart(2, '0')}5`;
  return setId.toUpperCase();
}

const TCG_SET_ID_TO_SPIRIT: Record<string, string> = (() => {
  const map: Record<string, string> = {};
  for (const [spirit, ids] of Object.entries(SPIRIT_TO_TCG_SET_IDS as Record<string, string[]>)) {
    for (const id of ids) {
      if (!map[id]) map[id] = spirit;
    }
  }
  return map;
})();

const rootDir = dirname(fileURLToPath(import.meta.url));
const repoRoot = join(rootDir, '../..');
const dataRoot = join(rootDir, 'data', 'pokemon-tcg-data');
const jpDataRoot = join(rootDir, 'data', 'limitless-jp');
const implementedCardIdsPath = join(rootDir, 'implementedCardIds.json');
const scriptsRoot = join(repoRoot, 'spirit/game/scripts/cards');
const assetsRoot = join(repoRoot, 'spirit/assets/cards');
const setsJsonPath = join(repoRoot, 'spirit/database/json_data/sets.json');
const formatsJsonPath = join(repoRoot, 'spirit/database/json_data/formats.json');

const FORMAT_GUIDS = {
  Standard: '6402e830-7fed-4cd1-b172-2a320047c2bb',
  Expanded: '98c83df9-ec82-4193-84a8-104115ce4e25',
  Legacy: '6b33d420-73cc-40d4-ada5-88a7d68063a9',
  Unlimited: '6a1dec5a-34db-4cee-a503-4ee759304135',
} as const;

/** Sets currently treated as Standard in formats.json / format_manager. */
const STANDARD_SET_RE = /^(SV0?5|SV0?6|SV065|SV0?7|SV0?8|SV085|SV0?9|SV10|CEL25|PGO|CZ)$/i;

function countScriptsInSet(spiritCode: string): number {
  const dir = join(scriptsRoot, spiritCode);
  if (!existsSync(dir)) return 0;
  return readdirSync(dir).filter(f => f.endsWith('.py') && f !== '__init__.py').length;
}

function loadCatalogSetMeta(catalogId?: string): {
  id: string;
  name: string;
  series: string;
  ptcgoCode?: string;
  total?: number;
  printedTotal?: number;
} | null {
  if (!catalogId) return null;
  const dash = catalogId.indexOf('-');
  if (dash <= 0) return null;
  const setId = catalogId.slice(0, dash);
  const setsFile = join(dataRoot, 'sets/en.json');
  if (!existsSync(setsFile)) return null;
  const sets = JSON.parse(readFileSync(setsFile, 'utf8')) as Array<{
    id: string;
    name: string;
    series: string;
    ptcgoCode?: string;
    total?: number;
    printedTotal?: number;
  }>;
  return sets.find(s => s.id === setId) || null;
}

function inferBlock(spiritCode: string, series?: string): string {
  const code = spiritCode.toUpperCase();
  if (code.startsWith('SV')) return 'SV';
  if (code.startsWith('SWSH')) return 'SWSH';
  if (code.startsWith('BW')) return 'BW';
  if (code.startsWith('SM')) return 'SM';
  if (code.startsWith('XY')) return 'XY';
  if (code.startsWith('HGSS')) return 'HGSS';
  const s = (series || '').toLowerCase();
  if (s.includes('scarlet') || s.includes('violet')) return 'SV';
  if (s.includes('sword') || s.includes('shield')) return 'SWSH';
  if (s.includes('black') || s.includes('white')) return 'BW';
  if (s.includes('sun') || s.includes('moon')) return 'SM';
  if (s.includes('xy') || s.includes('kalos')) return 'XY';
  return 'NONE';
}

function formatKeysForNewSet(spiritCode: string): Array<keyof typeof FORMAT_GUIDS> {
  const keys: Array<keyof typeof FORMAT_GUIDS> = ['Expanded', 'Unlimited'];
  if (
    STANDARD_SET_RE.test(spiritCode) ||
    /^SV(0?[5-9]|10|065|085)$/i.test(spiritCode)
  ) {
    keys.unshift('Standard');
  }
  if (/^BW/i.test(spiritCode)) keys.push('Legacy');
  return [...new Set(keys)];
}

function nextSetNumber(sets: Array<{ number: number }>): number {
  const max = Math.max(0, ...sets.map(s => (s.number < 9000 ? s.number : 0)));
  return max + 10;
}

/**
 * Ensures Spirit set folders exist and the set is indexed in sets.json + formats.json
 * so the client catalog / format legality can see it.
 */
function ensureSetRegistered(
  spiritCode: string,
  catalogId?: string
): { created: boolean; messages: string[] } {
  const messages: string[] = [];
  mkdirSync(join(scriptsRoot, spiritCode), { recursive: true });
  mkdirSync(join(assetsRoot, spiritCode), { recursive: true });

  const meta = loadCatalogSetMeta(catalogId);
  const scriptCount = countScriptsInSet(spiritCode);
  const formatKeys = formatKeysForNewSet(spiritCode);
  const legalFormats = formatKeys.map(k => FORMAT_GUIDS[k]);

  let created = false;
  if (existsSync(setsJsonPath)) {
    const sets = JSON.parse(readFileSync(setsJsonPath, 'utf8')) as Array<{
      name: string;
      externalId: string;
      number: number;
      count: number;
      filter: boolean;
      block: string;
      legalFormats: string[];
      featuredArchetypes: string[];
      visibleUnfilterable: boolean;
      promo: boolean;
    }>;
    const idx = sets.findIndex(s => String(s.name).toUpperCase() === spiritCode.toUpperCase());
    if (idx < 0) {
      const entry = {
        name: spiritCode,
        externalId: meta?.ptcgoCode || meta?.id?.toUpperCase() || spiritCode,
        number: nextSetNumber(sets),
        count: Math.max(scriptCount, 1),
        filter: true,
        block: inferBlock(spiritCode, meta?.series),
        legalFormats,
        featuredArchetypes: [] as string[],
        visibleUnfilterable: false,
        promo: /promo/i.test(spiritCode) || /promo/i.test(meta?.name || ''),
      };
      sets.push(entry);
      writeFileSync(setsJsonPath, `${JSON.stringify(sets, null, 2)}\n`, 'utf8');
      created = true;
      messages.push(`Registered ${spiritCode} in sets.json (block=${entry.block}, externalId=${entry.externalId}).`);
    } else {
      const prev = sets[idx];
      const nextCount = Math.max(prev.count || 0, scriptCount);
      let changed = false;
      if (nextCount !== prev.count) {
        prev.count = nextCount;
        changed = true;
      }
      for (const guid of legalFormats) {
        if (!prev.legalFormats.includes(guid)) {
          prev.legalFormats.push(guid);
          changed = true;
        }
      }
      if (changed) {
        writeFileSync(setsJsonPath, `${JSON.stringify(sets, null, 2)}\n`, 'utf8');
        messages.push(`Updated ${spiritCode} entry in sets.json (count=${prev.count}).`);
      }
    }
  } else {
    messages.push('sets.json missing — could not register set.');
  }

  if (existsSync(formatsJsonPath)) {
    const data = JSON.parse(readFileSync(formatsJsonPath, 'utf8')) as {
      formats: Array<{ key: string; sets: string[]; allSets?: boolean }>;
    };
    let formatsChanged = false;
    for (const fmt of data.formats || []) {
      if (fmt.allSets) continue; // Unlimited
      const shouldInclude =
        (fmt.key === 'Expanded' && formatKeys.includes('Expanded')) ||
        (fmt.key === 'Standard' && formatKeys.includes('Standard')) ||
        (fmt.key === 'Legacy' && formatKeys.includes('Legacy'));
      if (!shouldInclude) continue;
      if (!fmt.sets.includes(spiritCode)) {
        fmt.sets.push(spiritCode);
        formatsChanged = true;
        messages.push(`Added ${spiritCode} to formats.json ${fmt.key}.`);
      }
    }
    if (formatsChanged) {
      writeFileSync(formatsJsonPath, `${JSON.stringify(data, null, 2)}\n`, 'utf8');
    }
  }

  return { created, messages };
}

interface ScriptEffect {
  source: string;
  effectText: string;
  kind: 'attack' | 'power' | 'trainer' | 'energy';
  body: string[];
  imports: string[];
  similarity: number;
  helpers?: string[];
  fileName?: string;
  setCode?: string;
  displayName?: string;
  collectorNumber?: string;
  condition?: string;
  trigger?: string;
  activation?: string;
  passive?: string;
  sharedOncePerTurn?: string;
  locksNextTurn?: boolean;
}

function jsonResponse(res: ServerResponse, status: number, value: unknown): void {
  res.statusCode = status;
  res.setHeader('Content-Type', 'application/json; charset=utf-8');
  res.end(JSON.stringify(value));
}

function readRequestBody(req: IncomingMessage): Promise<string> {
  return new Promise((resolve, reject) => {
    const chunks: Buffer[] = [];
    req.on('data', chunk => chunks.push(Buffer.from(chunk)));
    req.on('end', () => resolve(Buffer.concat(chunks).toString('utf8')));
    req.on('error', reject);
  });
}

function collectPyFiles(dir: string): string[] {
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

function decodePyString(raw: string): string {
  try {
    return JSON.parse(raw.includes('"') || raw.startsWith("'") ? raw.replace(/^'/, '"').replace(/'$/, '"').replace(/\\'/g, "'") : raw);
  } catch {
    return raw.replace(/^['"]|['"]$/g, '').replace(/\\n/g, '\n').replace(/\\"/g, '"').replace(/\\'/g, "'");
  }
}

const PY_STRING = String.raw`(?:"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*')`;

function matchPyAttr(source: string, attr: string): string {
  const m = source.match(new RegExp(`${attr}\\s*=\\s*(${PY_STRING})`));
  return m ? decodePyString(m[1]) : '';
}

/** Read a Python assignment value, keeping nested parens instead of stopping at the first comma. */
function parsePyArgValue(body: string, attr: string): string {
  const re = new RegExp(`${attr}\\s*=\\s*`);
  const m = body.match(re);
  if (!m || m.index === undefined) return '';
  const start = m.index + m[0].length;
  let i = start;
  const open: string[] = [];
  let inStr: string | null = null;
  let escape = false;
  while (i < body.length) {
    const c = body[i];
    if (inStr) {
      if (escape) {
        escape = false;
        i += 1;
        continue;
      }
      if (c === '\\') {
        escape = true;
        i += 1;
        continue;
      }
      if (c === inStr) inStr = null;
      i += 1;
      continue;
    }
    if (c === '"' || c === "'") {
      inStr = c;
      i += 1;
      continue;
    }
    if (c === '(' || c === '[' || c === '{') {
      open.push(c);
      i += 1;
      continue;
    }
    if (c === ')' || c === ']' || c === '}') {
      if (!open.length) break;
      open.pop();
      i += 1;
      continue;
    }
    if (!open.length && (c === ',' || c === '\n')) break;
    i += 1;
  }
  if (open.length || inStr) return '';
  return body.slice(start, i).trim();
}

function isCompletePyExpr(expr: string): boolean {
  const trimmed = expr.trim();
  if (!trimmed || trimmed === 'unimplemented') return false;
  let depth = 0;
  let inStr: string | null = null;
  let escape = false;
  for (const c of trimmed) {
    if (inStr) {
      if (escape) {
        escape = false;
        continue;
      }
      if (c === '\\') {
        escape = true;
        continue;
      }
      if (c === inStr) inStr = null;
      continue;
    }
    if (c === '"' || c === "'") {
      inStr = c;
      continue;
    }
    if (c === '(') depth += 1;
    else if (c === ')') {
      depth -= 1;
      if (depth < 0) return false;
    }
  }
  return depth === 0 && !inStr;
}

function normalizeCardName(name: string): string {
  return name
    .normalize('NFKD')
    .replace(/[\u0300-\u036f]/g, '')
    .replace(/[’‘]/g, "'")
    .replace(/\s+/g, ' ')
    .trim()
    .toLowerCase();
}

function extractImports(source: string): string[] {
  return source
    .split('\n')
    .map(l => l.trim())
    .filter(l => /^from\s+\S+\s+import\s+/.test(l) || /^import\s+/.test(l));
}

function extractHelpersBeforeCard(source: string): string[] {
  const cardIdx = source.search(/\ncard\s*=/);
  if (cardIdx < 0) return [];
  const preamble = source.slice(0, cardIdx);
  const lines = preamble.split('\n');
  const helpers: string[] = [];
  let capturing = false;
  let buf: string[] = [];
  for (const line of lines) {
    if (/^(async\s+)?def\s+/.test(line) || /^[A-Z_][A-Z0-9_]*\s*=/.test(line)) {
      if (buf.length) helpers.push(buf.join('\n'));
      buf = [line];
      capturing = true;
      continue;
    }
    if (capturing) {
      if (/^from\s|^import\s|^#/.test(line) && buf.length === 0) {
        capturing = false;
        continue;
      }
      if (line.trim() === '' && buf.length > 0 && !/^\s/.test(line)) {
        helpers.push(buf.join('\n'));
        buf = [];
        capturing = false;
      } else {
        buf.push(line);
      }
    }
  }
  if (buf.length) helpers.push(buf.join('\n'));
  return helpers.filter(h => /^(async\s+)?def\s+/.test(h.trim()));
}

function extractCtxFactoryEffects(
  filePath: string,
  module: string,
  kind: ScriptEffect['kind']
): ScriptEffect[] {
  if (!existsSync(filePath)) return [];
  const source = readFileSync(filePath, 'utf8');
  const effects: ScriptEffect[] = [];
  const re =
    /^(async\s+)?def\s+([a-z][a-z0-9_]*)\s*\(\s*ctx\s*\)\s*:\s*\n\s*"""([\s\S]*?)"""/gm;
  let match: RegExpExecArray | null;
  while ((match = re.exec(source))) {
    const name = match[2];
    const effectText = match[3].replace(/\s+/g, ' ').trim();
    if (!effectText) continue;
    effects.push({
      source: `${module}.${name}`,
      effectText,
      kind,
      body: [name],
      imports: [`from ${module} import ${name}`],
      similarity: 0,
      helpers: [],
      fileName: name,
      setCode: '',
      displayName: name,
      collectorNumber: '',
    });
  }
  return effects;
}

function buildScriptEffects(): ScriptEffect[] {
  const effects: ScriptEffect[] = [];
  for (const file of collectPyFiles(scriptsRoot)) {
    const source = readFileSync(file, 'utf8');
    if (/\ncard\s*=\s*reprint\(/.test(source) || /^\s*card\s*=\s*reprint\(/.test(source)) continue;
    const rel = relative(scriptsRoot, file).replaceAll(sep, '/');
    const fileName = rel.split('/').pop() || '';
    const setCode =
      source.match(/set_code\s*=\s*["']([^"']+)["']/)?.[1] ||
      rel.split('/')[0] ||
      '';
    const displayName =
      matchPyAttr(source, 'display_name') ||
      matchPyAttr(source, 'name') ||
      '';
    const collectorNumber =
      source.match(/collector_number\s*=\s*(\d+)/)?.[1] ||
      fileName.match(/_(\d+)\.py$/)?.[1] ||
      '';
    const imports = extractImports(source);
    const helpers = extractHelpersBeforeCard(source);

    // Attack / Ability game_text + nearby effect=
    const abilityBlocks = [
      ...source.matchAll(
        /(?:Attack|Ability)\(\s*([\s\S]*?)(?=\n\s*(?:Attack|Ability)\(|\n\s*\],)/g
      ),
    ];
    for (const block of abilityBlocks) {
      const body = block[1] || '';
      const textRaw = body.match(/game_text\s*=\s*(("(?:\\.|[^"\\])*")|('(?:\\.|[^'\\])*'))/);
      if (!textRaw) continue;
      const effectText = decodePyString(textRaw[1]);
      if (!effectText.trim()) continue;
      const effectExpr = parsePyArgValue(body, 'effect');
      if (effectExpr && !isCompletePyExpr(effectExpr)) continue;
      const kind: ScriptEffect['kind'] = body.includes('cost=') || /damage\s*=/.test(body) ? 'attack' : 'power';
      const trigger = parsePyArgValue(body, 'trigger');
      const activation = parsePyArgValue(body, 'activation');
      const passive = parsePyArgValue(body, 'passive');
      const condition = parsePyArgValue(body, 'condition');
      const sharedRaw = parsePyArgValue(body, 'shared_once_per_turn');
      const sharedOncePerTurn = sharedRaw ? decodePyString(sharedRaw) || sharedRaw.replace(/^['"]|['"]$/g, '') : undefined;
      const locksNextTurn = /locks_next_turn\s*=\s*True/.test(body);
      if (!effectExpr && !passive && !locksNextTurn) continue;
      effects.push({
        source: rel,
        effectText,
        kind,
        body: effectExpr ? [effectExpr] : [],
        imports,
        similarity: 0,
        helpers: effectExpr && /^[a-z_][a-z0-9_]*$/i.test(effectExpr) ? helpers.filter(h => h.includes(`def ${effectExpr}`)) : [],
        fileName,
        setCode,
        displayName,
        collectorNumber,
        condition: condition || undefined,
        trigger: trigger || undefined,
        activation: activation || undefined,
        passive: passive || undefined,
        sharedOncePerTurn: sharedOncePerTurn || undefined,
        locksNextTurn: locksNextTurn || undefined,
      });
    }

    // Trainer / stadium top-level effect=
    if (/SupporterCardDef|ItemCardDef|StadiumCardDef|PokemonToolCardDef|FossilItemCardDef/.test(source)) {
      const effectExpr = parsePyArgValue(source, 'effect');
      const condition = parsePyArgValue(source, 'condition') || undefined;
      const trigger = parsePyArgValue(source, 'trigger') || undefined;
      let effectText = '';
      if (effectExpr && /^[a-z_][a-z0-9_]*$/i.test(effectExpr)) {
        const doc = source.match(
          new RegExp(
            `(?:async\\s+)?def\\s+${effectExpr}\\s*\\([^)]*\\)\\s*:\\s*\\n\\s*"""([\\s\\S]*?)"""`
          )
        );
        if (doc) effectText = doc[1].replace(/\s+/g, ' ').trim();
      }
      if (!effectText) {
        const gameText = source.match(/game_text\s*=\s*(("(?:\\.|[^"\\])*")|('(?:\\.|[^'\\])*'))/);
        if (gameText) effectText = decodePyString(gameText[1]);
      }
      if (!effectText) {
        const rulesText = source.match(/"""([\s\S]*?)"""/)?.[1]?.trim();
        if (rulesText) effectText = rulesText.replace(/\s+/g, ' ').trim();
      }
      if (effectExpr && effectText && isCompletePyExpr(effectExpr)) {
        const simpleName = /^[a-z_][a-z0-9_]*$/i.test(effectExpr);
        effects.push({
          source: rel,
          effectText,
          kind: 'trainer',
          body: [effectExpr],
          imports,
          similarity: 0,
          helpers: simpleName
            ? helpers.filter(
                h =>
                  h.includes(`def ${effectExpr}`) ||
                  new RegExp(`def\\s+_${effectExpr}\\b`).test(h)
              )
            : helpers.filter(h => /^(async\s+)?def\s+/.test(h.trim())),
          fileName,
          setCode,
          displayName,
          collectorNumber,
          condition,
          trigger,
        });
      }
    }

    if (/EnergyCardDef/.test(source)) {
      const texts = [...source.matchAll(/game_text\s*=\s*(("(?:\\.|[^"\\])*")|('(?:\\.|[^'\\])*'))/g)];
      for (const t of texts) {
        const effectText = decodePyString(t[1]);
        const effectMatch = source.match(/effect\s*=\s*([^,\n]+)/);
        effects.push({
          source: rel,
          effectText,
          kind: 'energy',
          body: effectMatch ? [effectMatch[1].trim()] : [],
          imports,
          similarity: 0,
          helpers,
          fileName,
          setCode,
          displayName,
          collectorNumber,
        });
      }
    }
  }
  effects.push(
    ...extractCtxFactoryEffects(
      join(repoRoot, 'spirit/game/card_effects/trainers.py'),
      'spirit.game.card_effects.trainers',
      'trainer'
    )
  );
  return effects;
}

function listSpiritSetDirs(): string[] {
  if (!existsSync(scriptsRoot)) return [];
  return readdirSync(scriptsRoot, { withFileTypes: true })
    .filter(e => e.isDirectory() && e.name !== '__pycache__' && e.name !== 'CUSTOM')
    .map(e => e.name);
}

function findReprintCandidates(spiritSet: string, name: string, excludeNumber = '') {
  const normalizedName = normalizeCardName(name);
  const exclude = excludeNumber.trim();
  const targetSet = spiritSet.trim().toUpperCase();
  const out: Array<{
    className: string;
    name: string;
    set: string;
    setNumber: string;
    fullName: string;
    sourcePath: string;
    fileName: string;
    category: 'pokemon' | 'trainer' | 'energy';
    reprintIdentity?: string | null;
  }> = [];

  for (const setDir of listSpiritSetDirs()) {
    const dir = join(scriptsRoot, setDir);
    for (const filePath of collectPyFiles(dir)) {
      const source = readFileSync(filePath, 'utf8');
      if (/^\s*card\s*=\s*reprint\(/.test(source) || /\ncard\s*=\s*reprint\(/.test(source)) continue;
      const displayName = matchPyAttr(source, 'display_name');
      if (!displayName || normalizeCardName(displayName) !== normalizedName) continue;
      const collectorNumber = source.match(/collector_number\s*=\s*(\d+)/)?.[1] || '';
      const fileName = filePath.split(/[/\\]/).pop() || '';
      const sourcePath = relative(scriptsRoot, filePath).replaceAll(sep, '/');
      if (setDir.toUpperCase() === targetSet && exclude && collectorNumber === exclude) continue;
      const isPokemon = /PokemonCardDef\s*\(/.test(source);
      const category: 'pokemon' | 'trainer' | 'energy' = isPokemon
        ? 'pokemon'
        : /EnergyCardDef\s*\(/.test(source)
          ? 'energy'
          : 'trainer';
      out.push({
        className: fileName.replace(/\.py$/, ''),
        name: displayName,
        set: setDir,
        setNumber: collectorNumber,
        fullName: `${displayName} ${setDir}`,
        sourcePath,
        fileName,
        category,
        reprintIdentity: isPokemon ? pokemonReprintIdentityFromScript(source) : undefined,
      });
    }
  }

  return out.sort((a, b) => {
    const aSame = a.set.toUpperCase() === targetSet ? 0 : 1;
    const bSame = b.set.toUpperCase() === targetSet ? 0 : 1;
    return aSame - bSame || a.set.localeCompare(b.set) || Number(a.setNumber) - Number(b.setNumber);
  });
}

function buildImplementedJpIndex(): {
  namesBySet: Record<string, string[]>;
  pokemonIdentitiesBySet: Record<string, string[]>;
} {
  const namesBySet: Record<string, Set<string>> = {};
  const pokemonIdentitiesBySet: Record<string, Set<string>> = {};
  const addName = (set: string, name: string) => {
    const key = identityName(name);
    if (!key) return;
    if (!namesBySet[set]) namesBySet[set] = new Set();
    namesBySet[set].add(key);
  };
  for (const setDir of listSpiritSetDirs()) {
    const set = setDir.toUpperCase();
    const dir = join(scriptsRoot, setDir);
    for (const filePath of collectPyFiles(dir)) {
      const source = readFileSync(filePath, 'utf8');
      const fileName = filePath.split(/[/\\]/).pop() || '';
      const displayName = matchPyAttr(source, 'display_name');
      if (displayName) addName(set, displayName);
      const fromFile = fileName.replace(/_\d+\.py$/i, '').replace(/\.py$/i, '');
      if (fromFile) addName(set, fromFile);
      if (/PokemonCardDef\s*\(/.test(source)) {
        const identity = pokemonReprintIdentityFromScript(source);
        if (identity) {
          if (!pokemonIdentitiesBySet[set]) pokemonIdentitiesBySet[set] = new Set();
          pokemonIdentitiesBySet[set].add(identity);
        }
      }
    }
  }
  const namesOut: Record<string, string[]> = {};
  const idOut: Record<string, string[]> = {};
  for (const [k, v] of Object.entries(namesBySet)) namesOut[k] = [...v];
  for (const [k, v] of Object.entries(pokemonIdentitiesBySet)) idOut[k] = [...v];
  return { namesBySet: namesOut, pokemonIdentitiesBySet: idOut };
}

function downloadFile(url: string, dest: string): Promise<void> {
  return new Promise((resolve, reject) => {
    const getter = url.startsWith('https') ? httpsGet : httpGet;
    const file = createWriteStream(dest);
    getter(url, res => {
      if (res.statusCode && res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
        file.close();
        downloadFile(res.headers.location, dest).then(resolve, reject);
        return;
      }
      if (res.statusCode !== 200) {
        file.close();
        reject(new Error(`HTTP ${res.statusCode} for ${url}`));
        return;
      }
      res.pipe(file);
      file.on('finish', () => file.close(() => resolve()));
    }).on('error', err => {
      file.close();
      reject(err);
    });
  });
}

function resolveSpiritSet(payloadSet: string, catalogId?: string): string {
  const upper = (payloadSet || '').trim().toUpperCase();
  if (catalogId) {
    const fromCat = spiritSetCodeFromCatalogId(catalogId);
    if (fromCat) return fromCat;
  }
  const spiritMap = SPIRIT_TO_TCG_SET_IDS as Record<string, string[]>;
  if (spiritMap[upper]) return upper;
  if (TCG_SET_ID_TO_SPIRIT[payloadSet?.toLowerCase()]) {
    return TCG_SET_ID_TO_SPIRIT[payloadSet.toLowerCase()];
  }
  return upper;
}

function spiritCardBuilderPlugin(): Plugin {
  return {
    name: 'spirit-card-builder-api',
    configureServer(server) {
      server.middlewares.use((req, res, next) => {
        const url = req.url?.split('?')[0] || '';

        if (url.startsWith('/tcg-data/')) {
          const rel = decodeURIComponent(url.slice('/tcg-data/'.length));
          const filePath = join(dataRoot, rel);
          if (!filePath.startsWith(dataRoot) || !existsSync(filePath)) {
            res.statusCode = 404;
            res.end('Not found');
            return;
          }
          if (filePath.endsWith('.json')) {
            res.setHeader('Content-Type', 'application/json; charset=utf-8');
          }
          res.end(readFileSync(filePath));
          return;
        }

        if (url === '/limitless-jp/sets.json') {
          void (async () => {
            try {
              jsonResponse(res, 200, await loadOrFetchSets(jpDataRoot));
            } catch (e) {
              jsonResponse(res, 502, { error: `Limitless JP index failed: ${e instanceof Error ? e.message : e}` });
            }
          })();
          return;
        }

        if (url.startsWith('/limitless-jp/cards/')) {
          const setId = decodeURIComponent(url.slice('/limitless-jp/cards/'.length)).replace(/\.json$/i, '');
          if (!/^[A-Za-z0-9]+$/.test(setId)) {
            jsonResponse(res, 400, { error: 'Invalid set id.' });
            return;
          }
          void (async () => {
            try {
              jsonResponse(res, 200, await loadOrFetchSetCards(jpDataRoot, setId));
            } catch (e) {
              jsonResponse(res, 502, { error: `Limitless JP set ${setId} failed: ${e instanceof Error ? e.message : e}` });
            }
          })();
          return;
        }

        if (url === '/limitless-jp/search' && req.method === 'GET') {
          const q = new URL(req.url || '', 'http://localhost').searchParams.get('q') || '';
          void (async () => {
            try {
              jsonResponse(res, 200, await searchLimitlessCards(jpDataRoot, q));
            } catch (e) {
              jsonResponse(res, 502, { error: `Limitless JP search failed: ${e instanceof Error ? e.message : e}` });
            }
          })();
          return;
        }

        if (url === '/implemented-jp.json') {
          jsonResponse(res, 200, buildImplementedJpIndex());
          return;
        }

        if (url === '/implemented-card-ids.json') {
          if (!existsSync(implementedCardIdsPath)) {
            jsonResponse(res, 200, { implementedCardIds: [] });
            return;
          }
          res.setHeader('Content-Type', 'application/json; charset=utf-8');
          res.end(readFileSync(implementedCardIdsPath));
          return;
        }

        if (url === '/server-card-effects.json') {
          try {
            jsonResponse(res, 200, buildScriptEffects());
          } catch (e) {
            jsonResponse(res, 500, { error: String(e) });
          }
          return;
        }

        if (url === '/reprint-candidates' && req.method === 'GET') {
          const u = new URL(req.url || '', 'http://localhost');
          const set = resolveSpiritSet(u.searchParams.get('set') || '');
          const name = u.searchParams.get('name')?.trim() || '';
          const excludeSetNumber = u.searchParams.get('excludeSetNumber')?.trim() || '';
          if (!set || !name) {
            jsonResponse(res, 400, { error: 'Set code and card name are required.' });
            return;
          }
          jsonResponse(res, 200, {
            candidates: findReprintCandidates(set, name, excludeSetNumber),
          });
          return;
        }

        if (url === '/save-card' && req.method === 'POST') {
          void (async () => {
            try {
              const payload = JSON.parse(await readRequestBody(req)) as {
                set?: string;
                catalogId?: string;
                fileName?: string;
                className?: string;
                source?: string;
                overwrite?: boolean;
                imageUrl?: string;
                downloadImage?: boolean;
                reprint?: {
                  fileName: string;
                  sourcePath: string;
                  name: string;
                  set: string;
                  setNumber: string;
                };
              };

              const spiritSet = resolveSpiritSet(payload.set || '', payload.catalogId);
              if (!/^[A-Z0-9][A-Z0-9_]*$/i.test(spiritSet)) {
                jsonResponse(res, 400, { error: 'Set code is invalid.' });
                return;
              }

              const dir = join(scriptsRoot, spiritSet);
              mkdirSync(dir, { recursive: true });
              mkdirSync(join(assetsRoot, spiritSet), { recursive: true });

              const warnings: string[] = [];

              const finishSave = (
                outPath: string,
                imagePath: string | undefined,
                label: string
              ) => {
                const reg = ensureSetRegistered(spiritSet, payload.catalogId);
                warnings.push(...reg.messages);
                jsonResponse(res, 200, {
                  message: `${label}${reg.created ? ` · registered set ${spiritSet}` : ''}`,
                  path: outPath,
                  imagePath,
                  warnings,
                  setRegistered: true,
                  setCreated: reg.created,
                });
              };

              if (payload.reprint) {
                const sourceRel = (payload.reprint.sourcePath || payload.reprint.fileName || '').replaceAll('\\', '/');
                const sourceAbs = join(scriptsRoot, sourceRel);
                if (!sourceRel || sourceAbs.includes('..') || !sourceAbs.startsWith(scriptsRoot) || !existsSync(sourceAbs)) {
                  jsonResponse(res, 400, { error: 'Reprint source script not found.' });
                  return;
                }
                const outName =
                  payload.fileName ||
                  `${String(payload.reprint.name || 'Card').replace(/[^a-zA-Z0-9]/g, '')}_${payload.reprint.setNumber}.py`;
                const outPath = join(dir, outName);
                if (existsSync(outPath) && !payload.overwrite) {
                  jsonResponse(res, 409, { error: 'File already exists.', path: outPath, warnings });
                  return;
                }
                if (!payload.source?.trim()) {
                  jsonResponse(res, 400, { error: 'Generated source is empty.' });
                  return;
                }
                writeFileSync(outPath, payload.source, 'utf8');
                let imagePath: string | undefined;
                if (payload.downloadImage !== false && payload.imageUrl) {
                  const stem = outName.replace(/\.py$/, '');
                  imagePath = join(assetsRoot, spiritSet, `${stem}.png`);
                  if (!existsSync(imagePath) || payload.overwrite) {
                    try {
                      await downloadFile(payload.imageUrl, imagePath);
                    } catch (e) {
                      warnings.push(`Image download failed: ${e}`);
                      imagePath = undefined;
                    }
                  }
                }
                finishSave(outPath, imagePath, `Saved reprint ${outName}`);
                return;
              }

              const fileName =
                payload.fileName ||
                `${String(payload.className || 'Card').replace(/[^a-zA-Z0-9]/g, '')}_0.py`;
              if (!/^[A-Za-z0-9_]+\.py$/.test(fileName)) {
                jsonResponse(res, 400, { error: 'Invalid file name.' });
                return;
              }
              if (!payload.source?.trim()) {
                jsonResponse(res, 400, { error: 'Generated source is empty.' });
                return;
              }
              const outPath = join(dir, fileName);
              if (existsSync(outPath) && !payload.overwrite) {
                jsonResponse(res, 409, { error: 'File already exists.', path: outPath, warnings });
                return;
              }
              writeFileSync(outPath, payload.source, 'utf8');

              let imagePath: string | undefined;
              if (payload.downloadImage !== false && payload.imageUrl) {
                const stem = fileName.replace(/\.py$/, '');
                imagePath = join(assetsRoot, spiritSet, `${stem}.png`);
                if (!existsSync(imagePath) || payload.overwrite) {
                  try {
                    await downloadFile(payload.imageUrl, imagePath);
                  } catch (e) {
                    warnings.push(`Image download failed: ${e}`);
                    imagePath = undefined;
                  }
                }
              }

              finishSave(outPath, imagePath, `Saved ${relative(repoRoot, outPath)}`);
            } catch (e) {
              jsonResponse(res, 500, { error: String(e) });
            }
          })();
          return;
        }

        next();
      });
    },
  };
}

export default defineConfig({
  root: rootDir,
  server: {
    port: 5174,
    strictPort: true,
  },
  plugins: [spiritCardBuilderPlugin()],
});

import type { AttackDraft, CardDraft, PowerDraft } from '../types';

/**
 * Gameplay identity for Pokémon reprints. Set, collector number, rarity,
 * art, and regulation mark are ignored — everything else must match.
 */

const TYPE_FROM_ENUM: Record<string, string> = {
  GRASS: 'G',
  FIRE: 'R',
  WATER: 'W',
  LIGHTNING: 'L',
  PSYCHIC: 'P',
  FIGHTING: 'F',
  DARKNESS: 'D',
  METAL: 'M',
  FAIRY: 'Y',
  DRAGON: 'N',
  COLORLESS: 'C',
  UNSET: '',
};

const STAGE_FROM_ENUM: Record<string, string> = {
  BASIC: 'BASIC',
  STAGE1: 'STAGE_1',
  STAGE_1: 'STAGE_1',
  STAGE2: 'STAGE_2',
  STAGE_2: 'STAGE_2',
  VMAX: 'VMAX',
  VSTAR: 'VSTAR',
  VUNION: 'VUNION',
  MEGA: 'MEGA',
  BREAK: 'BREAK',
  LEGEND: 'LEGEND',
  LV_X: 'LV_X',
  RESTORED: 'RESTORED',
  NONE: 'BASIC',
};

const PY_STRING = String.raw`(?:"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*')`;

const ENERGY_NAMES: Array<[RegExp, string]> = [
  [/\bcolorless\b/gi, '[c]'],
  [/\blightning\b/gi, '[l]'],
  [/\bdarkness\b/gi, '[d]'],
  [/\bfighting\b/gi, '[f]'],
  [/\bpsychic\b/gi, '[p]'],
  [/\bdragon\b/gi, '[n]'],
  [/\bgrass\b/gi, '[g]'],
  [/\bwater\b/gi, '[w]'],
  [/\bmetal\b/gi, '[m]'],
  [/\bfairy\b/gi, '[y]'],
  [/\bfire\b/gi, '[r]'],
];

function normalizeReprintText(text: string): string {
  let normalized = text
    .normalize('NFKD')
    .replace(/[\u0300-\u036f]/g, '')
    .replace(/[’‘]/g, "'")
    .replace(/[“”]/g, '"')
    .replace(/Pokémon/gi, 'Pokemon')
    .replace(/[\[{]([GRWLPFDMYNC])[\]}]/gi, (_, letter: string) => `[${letter.toLowerCase()}]`);
  for (const [pattern, token] of ENERGY_NAMES) {
    normalized = normalized.replace(pattern, token);
  }
  return normalized.replace(/\s+/g, ' ').trim().toLowerCase();
}

/** Compare printed names / evolves-from, including Spirit logic-name strings. */
export function identityName(value: string): string {
  const trimmed = value.trim();
  const fromLogic = trimmed.match(/\.([A-Za-z0-9]+)\.Name\s*$/)?.[1];
  return (fromLogic || trimmed).replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
}

function costKey(cost: string): string {
  return cost
    .toUpperCase()
    .replace(/ANY/g, 'A')
    .replace(/A/g, 'C')
    .replace(/[^GRWLPFDMYNC]/g, '')
    .split('')
    .sort()
    .join('');
}

function decodePyString(raw: string): string {
  try {
    return JSON.parse(
      raw.includes('"') || raw.startsWith("'")
        ? raw.replace(/^'/, '"').replace(/'$/, '"').replace(/\\'/g, "'")
        : raw
    );
  } catch {
    return raw.replace(/^['"]|['"]$/g, '').replace(/\\n/g, '\n').replace(/\\"/g, '"').replace(/\\'/g, "'");
  }
}

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

/** Join Python string literals, including parenthesized implicit concatenation. */
function joinPyStringLiterals(expr: string): string {
  if (!expr) return '';
  const parts: string[] = [];
  const re = new RegExp(PY_STRING, 'g');
  let m: RegExpExecArray | null;
  while ((m = re.exec(expr))) {
    parts.push(decodePyString(m[0]));
  }
  return parts.join('');
}

function pyStringAttr(body: string, attr: string): string {
  return joinPyStringLiterals(parsePyArgValue(body, attr));
}

function typeFromEnumExpr(expr: string): string {
  const name = expr.match(/PokemonTypes\.([A-Z_]+)/)?.[1] || '';
  return TYPE_FROM_ENUM[name] || '';
}

function stageFromEnumExpr(expr: string): string {
  const name = expr.match(/PokemonStage\.([A-Z0-9_]+)/)?.[1] || expr.replace(/[^A-Z0-9_]/g, '');
  return STAGE_FROM_ENUM[name] || name || 'BASIC';
}

function costFromPyDict(expr: string): string {
  if (!expr) return '';
  const parts: string[] = [];
  for (const m of expr.matchAll(/PokemonTypes\.([A-Z_]+)\s*:\s*(\d+)/g)) {
    const letter = TYPE_FROM_ENUM[m[1]] || '';
    const n = Number(m[2]) || 0;
    for (let i = 0; i < n; i++) parts.push(letter);
  }
  return costKey(parts.join(''));
}

function identityStageFromDraft(draft: CardDraft): string {
  const name = draft.name || '';
  const hasMega =
    draft.stage === 'MEGA' ||
    /\bmega\b/i.test(name) ||
    (draft.subtypes || []).some(s => /^mega$/i.test(s) || s === 'SV_Mega') ||
    /\bPOKEMON_SV_MEGA\b/.test(draft.tags || '');
  const hasSvEx =
    /\bex\b/.test(name) ||
    (draft.subtypes || []).includes('ex') ||
    /\bPOKEMON_SV_MEGA\b/.test(draft.tags || '');
  if ((hasMega && hasSvEx) || draft.stage === 'MEGA') {
    return draft.evolvesFrom ? 'STAGE_1' : 'BASIC';
  }
  return STAGE_FROM_ENUM[draft.stage] || draft.stage || 'BASIC';
}

function attackIdentity(attack: {
  name: string;
  cost: string;
  damage: string;
  damageCalculation?: string;
  text: string;
}): Record<string, string> {
  let damage = Number(attack.damage) || 0;
  let text = normalizeReprintText(attack.text);
  const snipe = text.match(
    /^this attack does (\d+) damage to 1 of your opponent's (benched )?pokemon\.?(?: \(don't apply weakness and resistance for benched pokemon\.\))?$/
  );
  if (snipe) {
    const amount = Number(snipe[1]);
    if (!damage) damage = amount;
    text = snipe[2] ? 'snipe bench' : '';
  }
  return {
    name: normalizeReprintText(attack.name),
    cost: costKey(attack.cost),
    damage: String(damage),
    op: attack.damageCalculation === '+' || attack.damageCalculation === 'x' ? attack.damageCalculation : '',
    text,
  };
}

function powerIdentity(power: { name: string; text: string }): Record<string, string> {
  return {
    name: normalizeReprintText(power.name),
    text: normalizeReprintText(power.text),
  };
}

function serializeIdentity(fields: {
  hp: string;
  type: string;
  stage: string;
  evolvesFrom: string;
  retreat: string;
  weakness: string;
  resistance: string;
  powers: Array<Record<string, string>>;
  attacks: Array<Record<string, string>>;
}): string {
  return JSON.stringify(fields);
}

export function pokemonReprintIdentityFromDraft(draft: CardDraft): string {
  const attacks = (draft.hasAttacks ? draft.attacks : [])
    .filter((a: AttackDraft) => a.enabled !== false)
    .map(a => attackIdentity(a));
  const powers = (draft.hasPowers ? draft.powers : []).map((p: PowerDraft) =>
    powerIdentity({ name: p.name, text: p.text })
  );
  return serializeIdentity({
    hp: String(Number(draft.hp) || 0),
    type: draft.cardType === 'A' ? 'C' : draft.cardType || '',
    stage: identityStageFromDraft(draft),
    evolvesFrom: identityName(draft.evolvesFrom || ''),
    retreat: String((draft.retreat || '').replace(/[^Cc]/g, '').length),
    weakness: draft.weaknessType || '',
    resistance: draft.resistanceType || '',
    powers,
    attacks,
  });
}

function parseAbilityBlocks(source: string): Array<{ kind: 'attack' | 'power'; body: string }> {
  const blocks: Array<{ kind: 'attack' | 'power'; body: string }> = [];
  const re = /(?:Attack|Ability)\(\s*([\s\S]*?)(?=\n\s*(?:Attack|Ability)\(|\n\s*\],)/g;
  let m: RegExpExecArray | null;
  while ((m = re.exec(source))) {
    const full = m[0];
    blocks.push({
      kind: /^\s*Attack\(/.test(full) ? 'attack' : 'power',
      body: m[1] || '',
    });
  }
  return blocks;
}

export function pokemonReprintIdentityFromScript(source: string): string | null {
  if (!/PokemonCardDef\s*\(/.test(source)) return null;

  const hp = parsePyArgValue(source, 'hp');
  const elements = parsePyArgValue(source, 'elements');
  const stage = parsePyArgValue(source, 'stage');
  const retreatRaw = parsePyArgValue(source, 'retreat_cost');
  const retreat = retreatRaw === '' ? '1' : retreatRaw;
  const weakness = parsePyArgValue(source, 'weakness_type');
  const resistance = parsePyArgValue(source, 'resistance_type');
  const evolvesFrom = pyStringAttr(source, 'evolves_from');

  const firstType = elements.match(/PokemonTypes\.([A-Z_]+)/)?.[1] || '';
  const powers: Array<Record<string, string>> = [];
  const attacks: Array<Record<string, string>> = [];

  for (const block of parseAbilityBlocks(source)) {
    if (block.kind === 'power') {
      powers.push(
        powerIdentity({
          name: pyStringAttr(block.body, 'title'),
          text: pyStringAttr(block.body, 'game_text'),
        })
      );
      continue;
    }
    const opRaw = pyStringAttr(block.body, 'damage_operator') || parsePyArgValue(block.body, 'damage_operator').replace(/^['"]|['"]$/g, '');
    attacks.push(
      attackIdentity({
        name: pyStringAttr(block.body, 'title'),
        cost: costFromPyDict(parsePyArgValue(block.body, 'cost')),
        damage: parsePyArgValue(block.body, 'damage') || '0',
        damageCalculation: opRaw === '+' || opRaw === 'x' ? opRaw : '',
        text: pyStringAttr(block.body, 'game_text'),
      })
    );
  }

  return serializeIdentity({
    hp: String(Number(hp) || 0),
    type: TYPE_FROM_ENUM[firstType] || '',
    stage: stageFromEnumExpr(stage),
    evolvesFrom: identityName(evolvesFrom),
    retreat: String(Number(retreat) || 0),
    weakness: typeFromEnumExpr(weakness),
    resistance: typeFromEnumExpr(resistance),
    powers,
    attacks,
  });
}

export function isIdenticalPokemonReprint(draft: CardDraft, scriptSource: string): boolean {
  const fromScript = pokemonReprintIdentityFromScript(scriptSource);
  if (!fromScript) return false;
  return pokemonReprintIdentityFromDraft(draft) === fromScript;
}

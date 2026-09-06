/** Hard constraints so similar-looking scripts are not reused for different cards. */

const ENERGY_TYPES = [
  'grass',
  'fire',
  'water',
  'lightning',
  'electric',
  'psychic',
  'fighting',
  'darkness',
  'dark',
  'metal',
  'steel',
  'fairy',
  'dragon',
  'colorless',
] as const;

const TYPE_ALIASES: Record<string, string> = {
  dark: 'darkness',
  electric: 'lightning',
  steel: 'metal',
};

const CONSTRAINT_PHRASES = [
  'fusion strike',
  'single strike',
  'rapid strike',
  'until you have',
  'more damage',
  'for each',
  'evolution',
  'pokemon ex',
  'pokemon v',
  'vmax',
  'vstar',
  'from your discard pile',
  'from your hand',
  'from your deck',
  'to evolve',
  'active spot',
  'weakness',
  'resistance',
  'non-',
];

const COMMON_PROPER = new Set([
  'once',
  'during',
  'your',
  'turn',
  'this',
  'pokemon',
  'energy',
  'basic',
  'stage',
  'active',
  'spot',
  'bench',
  'benched',
  'hand',
  'deck',
  'discard',
  'prize',
  'prizes',
  'damage',
  'attack',
  'ability',
  'weakness',
  'resistance',
  'special',
  'condition',
  'item',
  'supporter',
  'stadium',
  'tool',
  'then',
  'when',
  'you',
  'may',
  'put',
  'place',
  'draw',
  'search',
  'shuffle',
  'reveal',
  'attach',
  'switch',
  'heal',
  'flip',
  'heads',
  'tails',
  'coin',
  'more',
  'less',
  'each',
  'from',
  'into',
  'onto',
  'with',
  'that',
  'their',
  'opponent',
  'choose',
  'choice',
  'card',
  'cards',
  'counter',
  'counters',
  'before',
  'after',
  'applying',
  'affected',
  'mega',
  'either',
  'player',
  'players',
  'instead',
  'nothing',
  'paralyzed',
  'asleep',
  'confused',
  'poisoned',
  'burned',
  ...ENERGY_TYPES,
]);

function canonType(word: string): string {
  const key = word.toLowerCase();
  return TYPE_ALIASES[key] || key;
}

export function presentTypes(text: string): Set<string> {
  const found = new Set<string>();
  const lower = text.toLowerCase();
  for (const raw of ENERGY_TYPES) {
    const key = canonType(raw);
    const re = new RegExp(`\\b${raw}\\b`, 'i');
    if (re.test(lower)) found.add(key);
  }
  return found;
}

export function presentNumbers(text: string): number[] {
  const nums = [...text.matchAll(/\d+/g)].map(m => Number(m[0])).filter(n => Number.isFinite(n));
  return [...new Set(nums)].sort((a, b) => a - b);
}

function presentConstraints(text: string): Set<string> {
  const lower = text.toLowerCase();
  const found = new Set<string>();
  for (const phrase of CONSTRAINT_PHRASES) {
    if (lower.includes(phrase)) found.add(phrase);
  }
  return found;
}

/** Pokemon / mechanic names that must appear on both sides if present on either. */
export function properNames(text: string): Set<string> {
  const names = new Set<string>();
  const matches = text.match(/\b[A-Z][a-z]{2,}(?:[A-Z][a-z]+)?\b/g) || [];
  for (const raw of matches) {
    const key = raw.toLowerCase();
    if (COMMON_PROPER.has(key)) continue;
    if (ENERGY_TYPES.includes(key as (typeof ENERGY_TYPES)[number])) continue;
    names.add(key);
  }
  return names;
}

export function isBalancedExpr(expr: string): boolean {
  const trimmed = expr.trim();
  if (!trimmed) return false;
  if (trimmed === 'unimplemented') return false;
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

export function effectConstraintsMismatch(query: string, candidate: string): boolean {
  const qTypes = presentTypes(query);
  const cTypes = presentTypes(candidate);
  if (qTypes.size !== cTypes.size) return true;
  for (const t of qTypes) if (!cTypes.has(t)) return true;

  const qNums = presentNumbers(query);
  const cNums = presentNumbers(candidate);
  if (qNums.length !== cNums.length) return true;
  for (let i = 0; i < qNums.length; i += 1) {
    if (qNums[i] !== cNums[i]) return true;
  }

  const qCons = presentConstraints(query);
  const cCons = presentConstraints(candidate);
  for (const phrase of CONSTRAINT_PHRASES) {
    if (qCons.has(phrase) !== cCons.has(phrase)) return true;
  }

  const qNames = properNames(query);
  const cNames = properNames(candidate);
  for (const name of qNames) if (!cNames.has(name)) return true;
  for (const name of cNames) if (!qNames.has(name)) return true;

  return false;
}

export function isEvolveAbilityText(text: string): boolean {
  return /when you play this pok[eé]mon from your hand to evolve/i.test(text);
}

export function isOnPlayAbilityText(text: string): boolean {
  return /when you play this pok[eé]mon from your hand onto your bench/i.test(text);
}

export function isTriggeredAbilityText(text: string): boolean {
  return isEvolveAbilityText(text) || isOnPlayAbilityText(text);
}

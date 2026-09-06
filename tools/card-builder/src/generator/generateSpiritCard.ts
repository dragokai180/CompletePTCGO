import { getPrefabById } from '../prefabs/catalog';
import { MissingPrefabError, matchEffectText, matchEffectTextPartial, matchedToSelected } from '../prefabs/matcher';
import { isBalancedExpr, isTriggeredAbilityText } from '../prefabs/effectAccuracy';
import { findServerEffect } from '../serverEffects';
import type {
  AttackDraft,
  CardDraft,
  EffectKind,
  EnergyShort,
  PrefabImport,
  PowerDraft,
  SelectedPrefab,
  ServerEffect,
} from '../types';
import { spiritSetCodeFromPtcgoOrId } from './setMapping';
import { cleanCardName, spiritGuidForCatalogId } from './uuid5';
import { resolveTrainerEffect } from './composeTrainer';
import { effectFnName } from './effectFnName';
import { stripEnergyText } from '../trainerReminders';

const TYPE_ENUM: Record<EnergyShort, string> = {
  G: 'PokemonTypes.GRASS',
  R: 'PokemonTypes.FIRE',
  W: 'PokemonTypes.WATER',
  L: 'PokemonTypes.LIGHTNING',
  P: 'PokemonTypes.PSYCHIC',
  F: 'PokemonTypes.FIGHTING',
  D: 'PokemonTypes.DARKNESS',
  M: 'PokemonTypes.METAL',
  Y: 'PokemonTypes.FAIRY',
  N: 'PokemonTypes.DRAGON',
  C: 'PokemonTypes.COLORLESS',
  A: 'PokemonTypes.COLORLESS',
};

const STAGE_ENUM: Record<string, string> = {
  BASIC: 'PokemonStage.BASIC',
  STAGE_1: 'PokemonStage.STAGE1',
  STAGE_2: 'PokemonStage.STAGE2',
  VMAX: 'PokemonStage.VMAX',
  VSTAR: 'PokemonStage.VSTAR',
  VUNION: 'PokemonStage.VUNION',
  MEGA: 'PokemonStage.STAGE1',
  BREAK: 'PokemonStage.BREAK',
  LEGEND: 'PokemonStage.BASIC',
  LV_X: 'PokemonStage.STAGE1',
  RESTORED: 'PokemonStage.BASIC',
  NONE: 'PokemonStage.BASIC',
};

const RARITY_MAP: Record<string, string> = {
  Common: 'Rarities.Common',
  Uncommon: 'Rarities.Uncommon',
  Rare: 'Rarities.Rare',
  'Rare Holo': 'Rarities.RareHolo',
  'Rare Holo V': 'Rarities.RareHoloV',
  'Rare Holo VMAX': 'Rarities.RareHoloVMAX',
  'Rare Holo VSTAR': 'Rarities.RareHoloVSTAR',
  'Rare Holo EX': 'Rarities.RareHoloEX',
  'Double Rare': 'Rarities.RareHoloEX',
  'Rare Ultra': 'Rarities.RareUltra',
  'Rare Secret': 'Rarities.RareSecret',
  'Rare Rainbow': 'Rarities.RareRainbow',
  'Rare Promo': 'Rarities.RarePromo',
  Promo: 'Rarities.RarePromo',
  'Amazing Rare': 'Rarities.Amazing',
  'Radiant Rare': 'Rarities.RareRadiant',
  'Illustration Rare': 'Rarities.RareUltra',
  'Special Illustration Rare': 'Rarities.RareSecret',
  'Hyper Rare': 'Rarities.RareSecret',
  'ACE SPEC Rare': 'Rarities.Ace',
  'Ultra Rare': 'Rarities.RareUltra',
};

export function parseEnergyCost(input: string): EnergyShort[] {
  const cleaned = input.toUpperCase().replace(/ANY/g, 'A').replace(/[^GRWLPFDMYNCA]/g, '');
  return cleaned.split('') as EnergyShort[];
}

function pyStr(s: string): string {
  return JSON.stringify(s);
}

function mapRarity(raw: string): string {
  if (!raw) return 'Rarities.Common';
  if (RARITY_MAP[raw]) return RARITY_MAP[raw];
  if (/holo/i.test(raw)) return 'Rarities.RareHolo';
  if (/rare/i.test(raw)) return 'Rarities.Rare';
  if (/ace/i.test(raw)) return 'Rarities.Ace';
  return 'Rarities.Common';
}

function buildCostSrc(cost: string): string {
  const counts: Record<string, number> = {};
  for (const short of parseEnergyCost(cost)) {
    const enumRef = TYPE_ENUM[short] || 'PokemonTypes.COLORLESS';
    counts[enumRef] = (counts[enumRef] || 0) + 1;
  }
  return `{${Object.entries(counts).map(([k, v]) => `${k}: ${v}`).join(', ')}}`;
}

function mergeImports(imports: PrefabImport[]): string[] {
  const byModule = new Map<string, Set<string>>();
  for (const imp of imports) {
    if (!imp.module || !imp.names?.length) continue;
    const set = byModule.get(imp.module) ?? new Set();
    for (const n of imp.names) set.add(n);
    byModule.set(imp.module, set);
  }
  return [...byModule.entries()]
    .sort(([a], [b]) => a.localeCompare(b))
    .map(([mod, names]) => `from ${mod} import ${[...names].sort().join(', ')}`);
}

function uniqueFnName(base: string, used: Set<string>): string {
  let name = base;
  let n = 2;
  while (used.has(name)) {
    name = `${base}_${n}`;
    n += 1;
  }
  used.add(name);
  return name;
}

function renamePythonIdent(source: string, from: string, to: string): string {
  if (!from || from === to) return source;
  const escaped = from.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  return source
    .replace(new RegExp(`\\b${escaped}\\b`, 'g'), to)
    .replace(new RegExp(`_${escaped}\\b`, 'g'), `_${to}`);
}

function wrapDocstring(text: string, indent = '    ', width = 72): string {
  const words = text.replace(/\s+/g, ' ').trim().split(' ').filter(Boolean);
  const lines: string[] = [];
  let current = '';
  for (const word of words) {
    const next = current ? `${current} ${word}` : word;
    if (current && next.length > width) {
      lines.push(current);
      current = word;
    } else {
      current = next;
    }
  }
  if (current) lines.push(current);
  if (lines.length <= 1) return `"""${lines[0] || ''}"""`;
  return `"""${lines[0]}\n${lines.slice(1).map(l => indent + l).join('\n')}"""`;
}

function setHelperDocstring(helper: string, text: string): string {
  const formatted = wrapDocstring(text);
  if (/"""[\s\S]*?"""/.test(helper)) {
    return helper.replace(/"""[\s\S]*?"""/, formatted);
  }
  return helper.replace(/^((?:async\s+)?def\s+\w+\s*\([^)]*\)\s*:)[ \t]*\n/, `$1\n    ${formatted}\n`);
}

interface RetargetOpts {
  name: string;
  damage?: number;
  text?: string;
  usedFnNames: Set<string>;
}

/** When reusing a similar script's helper, rename `leaf_guard` to this card's attack/ability. */
function retargetCopiedHelpers(
  effectExpr: string | undefined,
  helpers: string[],
  opts: RetargetOpts
): { effectExpr?: string; helpers: string[] } {
  const simple = Boolean(effectExpr && /^[a-z_][a-z0-9_]*$/i.test(effectExpr));
  if (!simple || !helpers.length || !opts.name.trim()) {
    if (simple && effectExpr) opts.usedFnNames.add(effectExpr);
    return { effectExpr, helpers };
  }
  const desired = uniqueFnName(effectFnName(opts.name), opts.usedFnNames);
  const renamed = helpers.map(h => renamePythonIdent(h, effectExpr as string, desired));
  const docBody = [opts.damage ? `${opts.damage}.` : '', (opts.text || '').trim()].filter(Boolean).join(' ');
  if (!docBody) return { effectExpr: desired, helpers: renamed };
  const defRe = new RegExp(`^(?:async\\s+)?def\\s+${desired}\\b`, 'm');
  return {
    effectExpr: desired,
    helpers: renamed.map(h => (defRe.test(h) ? setHelperDocstring(h, docBody) : h)),
  };
}

function resolveSelectedEffect(
  selected: SelectedPrefab[],
  kind: EffectKind,
  index: number,
  name: string
): {
  effectExpr?: string;
  activation?: string;
  trigger?: string;
  passive?: string;
  sharedOncePerTurn?: string;
  locksNextTurn?: boolean;
  condition?: string;
  imports: PrefabImport[];
  helpers: string[];
  needsUnimplemented: boolean;
} {
  const imports: PrefabImport[] = [];
  const helpers: string[] = [];
  let effectExpr: string | undefined;
  let activation: string | undefined;
  let trigger: string | undefined;
  let passive: string | undefined;
  let sharedOncePerTurn: string | undefined;
  let locksNextTurn = false;
  let condition: string | undefined;
  let needsUnimplemented = false;
  const may = selected.some(s => s.prefabId === 'ON_EVOLVE' || s.prefabId === 'ON_PLAY');

  for (const sel of selected) {
    const prefab = getPrefabById(sel.prefabId);
    if (!prefab) continue;
    const params = { ...sel.params };
    if (may && (sel.prefabId === 'DRAW_CARDS' || sel.prefabId === 'GUST' || sel.prefabId === 'GUST_ABILITY')) {
      params.may = 'true';
    }
    const result = prefab.generateCall(params, { kind, index, attackName: name, powerName: name });
    if (result.imports) imports.push(...result.imports);
    if (result.helpers) helpers.push(...result.helpers);
    if (result.activation) activation = result.activation;
    if (result.trigger) trigger = result.trigger;
    if (result.passive) passive = result.passive;
    if (result.sharedOncePerTurn) sharedOncePerTurn = result.sharedOncePerTurn;
    if (result.locksNextTurn) locksNextTurn = true;
    if (result.condition) condition = result.condition;
    if (result.effectExpr) {
      if (effectExpr && effectExpr !== result.effectExpr) {
        needsUnimplemented = true;
        effectExpr = undefined;
      } else {
        effectExpr = result.effectExpr;
      }
    }
  }
  return {
    effectExpr,
    activation,
    trigger,
    passive,
    sharedOncePerTurn,
    locksNextTurn,
    condition,
    imports,
    helpers,
    needsUnimplemented,
  };
}

function effectFromServer(
  server?: ServerEffect,
  retarget?: RetargetOpts
): {
  effectExpr?: string;
  imports: PrefabImport[];
  helpers: string[];
  condition?: string;
  trigger?: string;
  activation?: string;
  passive?: string;
  sharedOncePerTurn?: string;
  locksNextTurn?: boolean;
} {
  if (!server) return { imports: [], helpers: [] };
  const imports: PrefabImport[] = [];
  for (const line of server.imports) {
    const m = line.match(/^from\s+(\S+)\s+import\s+(.+)$/);
    if (m) {
      imports.push({
        module: m[1],
        names: m[2].split(',').map(s => s.trim()).filter(Boolean),
      });
    }
  }
  const body = server.body.filter(Boolean);
  const joined = body.join('\n').trim();
  const exprMatch = joined.match(/^effect\s*=\s*(.+)$/m);
  let effectExpr = exprMatch ? exprMatch[1].trim() : body.length === 1 ? body[0].trim() : undefined;
  if (effectExpr && !isBalancedExpr(effectExpr)) {
    effectExpr = undefined;
  }
  const helpers = server.helpers || [];
  const extra = {
    condition: server.condition,
    trigger: server.trigger,
    activation: server.activation,
    passive: server.passive,
    sharedOncePerTurn: server.sharedOncePerTurn,
    locksNextTurn: server.locksNextTurn,
  };
  if (retarget) {
    const retargeted = retargetCopiedHelpers(effectExpr, helpers, retarget);
    return {
      effectExpr: retargeted.effectExpr,
      imports,
      helpers: retargeted.helpers,
      ...extra,
    };
  }
  return { effectExpr, imports, helpers, ...extra };
}

function uniqueSimpleHelper(
  effectExpr: string | undefined,
  helpers: string[],
  usedFnNames: Set<string>
): { effectExpr?: string; helpers: string[] } {
  if (!effectExpr || !/^[a-z_][a-z0-9_]*$/i.test(effectExpr)) {
    return { effectExpr, helpers };
  }
  const desired = uniqueFnName(effectExpr, usedFnNames);
  if (desired === effectExpr) return { effectExpr, helpers };
  return {
    effectExpr: desired,
    helpers: helpers.map(h => renamePythonIdent(h, effectExpr, desired)),
  };
}

function formatAttackBlock(
  attack: AttackDraft,
  index: number,
  usedFnNames: Set<string>
): { lines: string[]; imports: PrefabImport[]; usesUnimplemented: boolean; helpers: string[] } {
  const imports: PrefabImport[] = [];
  const helpers: string[] = [];
  let usesUnimplemented = false;
  const lines: string[] = ['        Attack('];
  lines.push(`            title=${pyStr(attack.name)},`);
  if (attack.text.trim()) {
    lines.push(`            game_text=${pyStr(attack.text.trim())},`);
  }
  lines.push(`            cost=${buildCostSrc(attack.cost)},`);
  const damage = Number(attack.damage) || 0;
  if (damage) lines.push(`            damage=${damage},`);
  if (attack.damageCalculation === '+' || attack.damageCalculation === 'x') {
    lines.push(`            damage_operator=${pyStr(attack.damageCalculation)},`);
  }

  const text = attack.text.trim();
  if (text) {
    if (attack.serverEffect) {
      const fromServer = effectFromServer(attack.serverEffect, {
        name: attack.name,
        damage,
        text,
        usedFnNames,
      });
      imports.push(...fromServer.imports);
      helpers.push(...fromServer.helpers);
      if (fromServer.locksNextTurn) {
        lines.push('            locks_next_turn=True,');
      }
      if (fromServer.effectExpr) {
        lines.push(`            effect=${fromServer.effectExpr},`);
      } else if (!fromServer.locksNextTurn) {
        lines.push('            effect=unimplemented,');
        usesUnimplemented = true;
      }
    } else {
      const resolved = resolveSelectedEffect(attack.selectedPrefabs, 'attack', index, attack.name);
      imports.push(...resolved.imports);
      const adopted = uniqueSimpleHelper(resolved.effectExpr, resolved.helpers, usedFnNames);
      helpers.push(...adopted.helpers);
      if (resolved.locksNextTurn) {
        lines.push('            locks_next_turn=True,');
      }
      const hasBody = Boolean(adopted.effectExpr) || resolved.locksNextTurn;
      if (resolved.needsUnimplemented || (!hasBody && attack.selectedPrefabs.length === 0)) {
        lines.push('            effect=unimplemented,');
        usesUnimplemented = true;
      } else if (adopted.effectExpr) {
        lines.push(`            effect=${adopted.effectExpr},`);
      }
    }
  }
  lines.push('        ),');
  return { lines, imports, usesUnimplemented, helpers };
}

function emitAbilityMeta(
  lines: string[],
  imports: PrefabImport[],
  opts: {
    trigger?: string;
    activation?: string;
    sharedOncePerTurn?: string;
    condition?: string;
    passive?: string;
    text: string;
    useWhenInPlay: boolean;
  }
): void {
  if (opts.trigger) {
    lines.push(`            trigger=${opts.trigger},`);
    imports.push({ module: 'spirit.game.data_utils', names: ['Triggers'] });
  } else if (opts.activation) {
    lines.push(`            activation=${opts.activation},`);
    imports.push({ module: 'spirit.game.data_utils', names: ['Activations'] });
  } else if (
    /once during your turn/i.test(opts.text) &&
    opts.useWhenInPlay &&
    !isTriggeredAbilityText(opts.text)
  ) {
    lines.push('            activation=Activations.ONCE_PER_TURN,');
    imports.push({ module: 'spirit.game.data_utils', names: ['Activations'] });
  }
  if (opts.sharedOncePerTurn) {
    lines.push(`            shared_once_per_turn=${pyStr(opts.sharedOncePerTurn)},`);
  }
  if (opts.condition) {
    lines.push(`            condition=${opts.condition},`);
  }
  if (opts.passive) {
    lines.push(`            passive=${opts.passive},`);
  }
}

function formatAbilityBlock(
  power: PowerDraft,
  index: number,
  usedFnNames: Set<string>
): { lines: string[]; imports: PrefabImport[]; usesUnimplemented: boolean; helpers: string[] } {
  const imports: PrefabImport[] = [];
  const helpers: string[] = [];
  let usesUnimplemented = false;
  const lines: string[] = ['        Ability('];
  lines.push(`            title=${pyStr(power.name)},`);
  if (power.text.trim()) {
    lines.push(`            game_text=${pyStr(power.text.trim())},`);
  }

  if (power.serverEffect) {
    const fromServer = effectFromServer(power.serverEffect, {
      name: power.name,
      text: power.text.trim(),
      usedFnNames,
    });
    imports.push(...fromServer.imports);
    helpers.push(...fromServer.helpers);
    const resolved = resolveSelectedEffect(power.selectedPrefabs, 'power', index, power.name);
    imports.push(...resolved.imports);
    helpers.push(...resolved.helpers);
    emitAbilityMeta(lines, imports, {
      trigger: fromServer.trigger || resolved.trigger,
      activation: fromServer.activation || resolved.activation,
      sharedOncePerTurn: fromServer.sharedOncePerTurn || resolved.sharedOncePerTurn,
      condition: fromServer.condition || resolved.condition,
      passive: fromServer.passive || resolved.passive,
      text: power.text,
      useWhenInPlay: power.useWhenInPlay,
    });
    if (fromServer.passive && !fromServer.effectExpr) {
      // passive-only
    } else if (fromServer.effectExpr) {
      lines.push(`            effect=${fromServer.effectExpr},`);
    } else {
      lines.push('            effect=unimplemented,');
      usesUnimplemented = true;
    }
  } else {
    const resolved = resolveSelectedEffect(power.selectedPrefabs, 'power', index, power.name);
    imports.push(...resolved.imports);
    const adopted = uniqueSimpleHelper(resolved.effectExpr, resolved.helpers, usedFnNames);
    helpers.push(...adopted.helpers);
    emitAbilityMeta(lines, imports, {
      trigger: resolved.trigger,
      activation: resolved.activation,
      sharedOncePerTurn: resolved.sharedOncePerTurn,
      condition: resolved.condition,
      passive: resolved.passive,
      text: power.text,
      useWhenInPlay: power.useWhenInPlay,
    });
    const hasBody = Boolean(adopted.effectExpr) || Boolean(resolved.passive);
    if (resolved.needsUnimplemented || (!hasBody && power.text.trim())) {
      lines.push('            effect=unimplemented,');
      usesUnimplemented = true;
    } else if (adopted.effectExpr) {
      lines.push(`            effect=${adopted.effectExpr},`);
    }
  }
  lines.push('        ),');
  return { lines, imports, usesUnimplemented, helpers };
}

function logicName(kind: 'pokemon' | 'trainer', safeName: string): string {
  return `com.direwolfdigital.cake.data.archetypes.${kind}.${safeName}.Name`;
}

function trainerClass(type: CardDraft['trainerType']): string {
  if (type === 'SUPPORTER') return 'SupporterCardDef';
  if (type === 'STADIUM') return 'StadiumCardDef';
  if (type === 'TOOL') return 'PokemonToolCardDef';
  return 'ItemCardDef';
}

/** SV Mega Evolution Pokémon ex, distinct from XY-era MEGA. */
function isSvMegaDraft(draft: CardDraft): boolean {
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
  return hasMega && hasSvEx;
}

function inferredPokemonSubtypes(draft: CardDraft): string[] {
  if (draft.stage === 'STAGE_1') return ['Stage 1'];
  if (draft.stage === 'MEGA') return draft.evolvesFrom ? ['Stage 1'] : ['Basic'];
  if (draft.stage === 'STAGE_2') return ['Stage 2'];
  if (draft.stage === 'VMAX') return ['VMAX'];
  if (draft.stage === 'VSTAR') return ['VSTAR'];
  return ['Basic'];
}

function pokemonSubtypes(draft: CardDraft): string[] {
  let subtypes = draft.subtypes?.length ? [...draft.subtypes] : inferredPokemonSubtypes(draft);
  if (isSvMegaDraft(draft)) {
    subtypes = subtypes.map(s => (s === 'MEGA' ? 'SV_Mega' : s));
    if (!subtypes.includes('SV_Mega')) subtypes.push('SV_Mega');
    if (draft.evolvesFrom) {
      subtypes = subtypes.filter(s => s !== 'Basic');
      if (!subtypes.includes('Stage 1')) subtypes.unshift('Stage 1');
    } else {
      subtypes = subtypes.filter(s => s !== 'Stage 1');
      if (!subtypes.includes('Basic')) subtypes.unshift('Basic');
    }
  }
  return [...new Set(subtypes.filter(Boolean))];
}

function spiritStageExpr(draft: CardDraft): string {
  if (isSvMegaDraft(draft) || draft.stage === 'MEGA') {
    return draft.evolvesFrom ? 'PokemonStage.STAGE1' : 'PokemonStage.BASIC';
  }
  return STAGE_ENUM[draft.stage] || 'PokemonStage.BASIC';
}

export function scriptFileName(draft: CardDraft): string {
  const safe = cleanCardName(draft.name || draft.className || 'Card');
  const num = String(draft.setNumber || '0').replace(/^0+(?=\d)/, '') || '0';
  return `${safe}_${num}.py`;
}

export function resolveSpiritSetCode(draft: CardDraft): string {
  if (draft.spiritSetCode?.trim()) return draft.spiritSetCode.trim().toUpperCase();
  return spiritSetCodeFromPtcgoOrId(draft.set, draft.catalogId);
}

/**
 * Auto-fill selectedPrefabs from effect text when empty; fall back to similar scripts.
 */
export async function resolvePrefabs(draft: CardDraft): Promise<CardDraft> {
  const next: CardDraft = structuredClone(draft);

  if (next.hasAttacks) {
    for (const attack of next.attacks) {
      const text = attack.text.trim();
      if (!text) {
        attack.matchError = undefined;
        continue;
      }
      if (attack.selectedPrefabs.length > 0) {
        attack.matchError = undefined;
        attack.serverEffect = undefined;
        continue;
      }
      try {
        const matched = matchEffectText(text, 'attack');
        attack.selectedPrefabs = matchedToSelected(matched);
        attack.matchError = undefined;
        attack.serverEffect = undefined;
      } catch (e) {
        if (e instanceof MissingPrefabError) {
          attack.selectedPrefabs = [];
          attack.matchError = undefined;
          attack.serverEffect = await findServerEffect(text, 'attack');
          continue;
        }
        throw e;
      }
    }
  }

  if (next.hasPowers) {
    for (const power of next.powers) {
      const text = power.text.trim();
      if (!text) {
        power.matchError = undefined;
        continue;
      }
      if (power.selectedPrefabs.length > 0) {
        power.matchError = undefined;
        power.serverEffect = undefined;
        continue;
      }
      try {
        const matched = matchEffectText(text, 'power');
        power.selectedPrefabs = matchedToSelected(matched);
        power.matchError = undefined;
        power.serverEffect = undefined;
      } catch (e) {
        if (e instanceof MissingPrefabError) {
          power.selectedPrefabs = [];
          power.matchError = undefined;
          power.serverEffect = await findServerEffect(text, 'power');
          continue;
        }
        throw e;
      }
    }
  }

  if (next.extends === 'TrainerCard') {
    const text = next.trainerText.trim();
    if (text && next.trainerPrefabs.length === 0) {
      const resolved = await resolveTrainerEffect(text, next.name || next.className || 'Trainer');
      next.trainerPrefabs = resolved.prefabs;
      next.trainerServerEffect = resolved.serverEffect;
    }
  }

  if (next.extends === 'EnergyCard') {
    const text = stripEnergyText(next.energyText.trim());
    if (text && (next.energyPrefabs || []).length === 0 && !next.energyServerEffect) {
      const partial = matchEffectTextPartial(text, 'energy');
      if (partial.matched.length && partial.unmatched.length === 0) {
        next.energyPrefabs = matchedToSelected(partial.matched);
      } else {
        next.energyServerEffect = await findServerEffect(text, 'energy');
      }
    }
  }

  return next;
}

export async function generateCardSource(draft: CardDraft): Promise<string> {
  const resolved = await resolvePrefabs(draft);
  const setCode = resolveSpiritSetCode(resolved);
  const safeName = cleanCardName(resolved.name || resolved.className || 'Card');
  const collector = Number(String(resolved.setNumber).replace(/\D/g, '')) || 0;
  const catalogId =
    resolved.catalogId ||
    `${setCode.toLowerCase()}-${resolved.setNumber}`;
  const guid = await spiritGuidForCatalogId(catalogId);
  const rarity = mapRarity(resolved.rarity);
  const subtypes =
    resolved.extends === 'PokemonCard'
      ? pokemonSubtypes(resolved)
      : resolved.subtypes?.length
        ? resolved.subtypes
        : resolved.extends === 'TrainerCard'
          ? [resolved.trainerType === 'SUPPORTER' ? 'Supporter' : resolved.trainerType === 'STADIUM' ? 'Stadium' : resolved.trainerType === 'TOOL' ? 'Pokémon Tool' : 'Item']
          : [resolved.energyType === 'SPECIAL' ? 'Special' : 'Basic'];

  const searchable = [resolved.name, ...subtypes, safeName];
  const allImports: PrefabImport[] = [];
  const helperBlocks: string[] = [];
  const usedFnNames = new Set<string>();
  let usesUnimplemented = false;

  if (resolved.extends === 'PokemonCard') {
    const abilityLines: string[] = [];
    if (resolved.hasPowers) {
      resolved.powers.forEach((p, i) => {
        const block = formatAbilityBlock(p, i, usedFnNames);
        abilityLines.push(...block.lines);
        allImports.push(...block.imports);
        helperBlocks.push(...block.helpers);
        if (block.usesUnimplemented) usesUnimplemented = true;
      });
    }
    if (resolved.hasAttacks) {
      resolved.attacks.forEach((a, i) => {
        const block = formatAttackBlock(a, i, usedFnNames);
        abilityLines.push(...block.lines);
        allImports.push(...block.imports);
        helperBlocks.push(...block.helpers);
        if (block.usesUnimplemented) usesUnimplemented = true;
      });
    }

    const dataNames = new Set<string>(['PokemonCardDef', 'Attack']);
    if (resolved.hasPowers) dataNames.add('Ability');
    if (usesUnimplemented) dataNames.add('unimplemented');
    for (const imp of allImports) {
      if (imp.module === 'spirit.game.data_utils') {
        for (const n of imp.names) dataNames.add(n);
      }
    }

    const attrNames = new Set<string>(['PokemonTypes', 'PokemonStage', 'Rarities']);
    for (const imp of allImports) {
      if (imp.module === 'spirit.game.attributes') {
        for (const n of imp.names) attrNames.add(n);
      }
    }

    const otherImports = mergeImports(
      allImports.filter(i => i.module !== 'spirit.game.data_utils' && i.module !== 'spirit.game.attributes')
    );

    const retreat = Math.max(0, parseEnergyCost(resolved.retreat).length);
    const element = TYPE_ENUM[resolved.cardType] || 'PokemonTypes.COLORLESS';
    const stage = spiritStageExpr(resolved);

    const lines: string[] = [
      `from spirit.game.data_utils import ${[...dataNames].sort((a, b) => {
        const order = ['PokemonCardDef', 'Attack', 'Ability', 'Activations', 'Triggers', 'unimplemented', 'is_pokemon_ex'];
        return (order.indexOf(a) === -1 ? 99 : order.indexOf(a)) - (order.indexOf(b) === -1 ? 99 : order.indexOf(b)) || a.localeCompare(b);
      }).join(', ')}`,
      `from spirit.game.attributes import ${[...attrNames].sort().join(', ')}`,
      ...otherImports,
      '',
    ];
    if (helperBlocks.length) {
      lines.push(...helperBlocks, '');
    }
    lines.push('card = PokemonCardDef(');
    lines.push(`    guid=${pyStr(guid)},`);
    lines.push(`    key=${pyStr(setCode)},`);
    lines.push(`    name=${pyStr(logicName('pokemon', safeName))},`);
    lines.push(`    display_name=${pyStr(resolved.name)},`);
    lines.push(`    searchable_by=${JSON.stringify(searchable)},`);
    lines.push(`    subtypes=${JSON.stringify(subtypes)},`);
    lines.push(`    collector_number=${collector},`);
    lines.push(`    set_code=${pyStr(setCode)},`);
    if (resolved.regulationMark) {
      lines.push(`    regulation_mark=${pyStr(resolved.regulationMark)},`);
    }
    lines.push(`    rarity=${rarity},`);
    lines.push(`    hp=${Number(resolved.hp) || 0},`);
    lines.push(`    elements=[${element}],`);
    lines.push(`    stage=${stage},`);
    lines.push(`    retreat_cost=${retreat},`);
    if (resolved.weaknessType) {
      lines.push(`    weakness_type=${TYPE_ENUM[resolved.weaknessType]},`);
    }
    if (resolved.resistanceType) {
      lines.push(`    resistance_type=${TYPE_ENUM[resolved.resistanceType]},`);
    }
    if (resolved.evolvesFrom) {
      lines.push(
        `    evolves_from=${pyStr(logicName('pokemon', cleanCardName(resolved.evolvesFrom)))},`
      );
    }
    if (resolved.familyId) {
      lines.push(`    family_id=${Number(resolved.familyId) || resolved.familyId},`);
    }
    if (abilityLines.length) {
      lines.push('    abilities=[');
      lines.push(...abilityLines);
      lines.push('    ],');
    }
    lines.push(')');
    return lines.join('\n') + '\n';
  }

  if (resolved.extends === 'TrainerCard') {
    const cls = trainerClass(resolved.trainerType);
    const dataNames = new Set<string>([cls]);
    let effectExpr: string | undefined;
    let helpers: string[] = [];
    let condition: string | undefined;
    let trigger: string | undefined;
    let stadiumPassive: string | undefined;

    if (resolved.trainerServerEffect) {
      const fromServer = effectFromServer(resolved.trainerServerEffect, {
        name: resolved.name,
        text: resolved.trainerText.trim(),
        usedFnNames,
      });
      allImports.push(...fromServer.imports);
      helpers = fromServer.helpers;
      effectExpr = fromServer.effectExpr;
      condition = fromServer.condition;
      trigger = fromServer.trigger;
      stadiumPassive = fromServer.passive;
    } else {
      const resolvedFx = resolveSelectedEffect(resolved.trainerPrefabs, 'trainer', 0, resolved.name);
      allImports.push(...resolvedFx.imports);
      const adopted = uniqueSimpleHelper(resolvedFx.effectExpr, resolvedFx.helpers, usedFnNames);
      helpers = adopted.helpers;
      effectExpr = adopted.effectExpr;
      condition = resolvedFx.condition;
      trigger = resolvedFx.trigger;
      stadiumPassive = resolvedFx.passive;
      if (resolvedFx.needsUnimplemented) usesUnimplemented = true;
    }

    const stadiumAbility = resolved.trainerType === 'STADIUM' && Boolean(trigger);
    if (!effectExpr && !stadiumAbility && !stadiumPassive) {
      usesUnimplemented = true;
      effectExpr = 'unimplemented';
    }
    if (usesUnimplemented || effectExpr === 'unimplemented') dataNames.add('unimplemented');
    if (stadiumAbility) {
      dataNames.add('Ability');
      dataNames.add('Triggers');
    }

    for (const imp of allImports) {
      if (imp.module === 'spirit.game.data_utils') {
        for (const n of imp.names) dataNames.add(n);
      }
    }
    const attrNames = new Set<string>(['Rarities']);
    for (const imp of allImports) {
      if (imp.module === 'spirit.game.attributes') {
        for (const n of imp.names) attrNames.add(n);
      }
    }
    const otherImports = mergeImports(
      allImports.filter(i => i.module !== 'spirit.game.data_utils' && i.module !== 'spirit.game.attributes')
    );

    const lines: string[] = [
      `from spirit.game.data_utils import ${[...dataNames].join(', ')}`,
      `from spirit.game.attributes import ${[...attrNames].sort().join(', ')}`,
      ...otherImports,
      '',
    ];
    if (helpers.length) {
      lines.push(...helpers, '');
    }
    lines.push(`card = ${cls}(`);
    lines.push(`    guid=${pyStr(guid)},`);
    lines.push(`    key=${pyStr(setCode)},`);
    lines.push(`    name=${pyStr(logicName('trainer', safeName))},`);
    lines.push(`    display_name=${pyStr(resolved.name)},`);
    lines.push(`    searchable_by=${JSON.stringify(searchable)},`);
    lines.push(`    subtypes=${JSON.stringify(subtypes)},`);
    lines.push(`    collector_number=${collector},`);
    lines.push(`    set_code=${pyStr(setCode)},`);
    if (resolved.regulationMark) {
      lines.push(`    regulation_mark=${pyStr(resolved.regulationMark)},`);
    }
    lines.push(`    rarity=${rarity},`);
    if (stadiumAbility) {
      lines.push('    abilities=[');
      lines.push('        Ability(');
      lines.push(`            title=${pyStr(resolved.name)},`);
      if (resolved.trainerText.trim()) {
        lines.push(`            game_text=${pyStr(resolved.trainerText.trim())},`);
      }
      lines.push(`            trigger=${trigger},`);
      lines.push(`            effect=${effectExpr},`);
      lines.push('        ),');
      lines.push('    ],');
    } else if (stadiumPassive) {
      lines.push(`    passive=${stadiumPassive}`);
    } else if (condition) {
      lines.push(`    effect=${effectExpr},`);
      lines.push(`    condition=${condition}`);
    } else {
      lines.push(`    effect=${effectExpr}`);
    }
    lines.push(')');
    return lines.join('\n') + '\n';
  }

  // Energy
  {
    const isSpecial = resolved.energyType === 'SPECIAL';
    const energyType = TYPE_ENUM[(resolved.provides?.[0] as EnergyShort) || resolved.cardType] || 'PokemonTypes.COLORLESS';
    let effectImports: PrefabImport[] = [];
    let helpers: string[] = [];
    let onAttach = '';
    let energyPassive = '';

    if (resolved.energyServerEffect) {
      const fromServer = effectFromServer(resolved.energyServerEffect, {
        name: resolved.name,
        text: resolved.energyText.trim(),
        usedFnNames,
      });
      effectImports = fromServer.imports;
      helpers = fromServer.helpers;
      onAttach = fromServer.effectExpr || '';
      energyPassive = fromServer.passive || '';
    } else if ((resolved.energyPrefabs || []).length) {
      const resolvedFx = resolveSelectedEffect(resolved.energyPrefabs, 'energy', 0, resolved.name);
      effectImports = resolvedFx.imports;
      helpers = resolvedFx.helpers;
      onAttach = resolvedFx.effectExpr || '';
      energyPassive = resolvedFx.passive || '';
    }

    const attrNames = new Set<string>(['PokemonTypes', 'Rarities']);
    for (const imp of effectImports) {
      if (imp.module === 'spirit.game.attributes') {
        for (const n of imp.names) attrNames.add(n);
      }
    }
    const otherImports = mergeImports(
      effectImports.filter(i => i.module !== 'spirit.game.attributes' && i.module !== 'spirit.game.data_utils')
    );

    const lines: string[] = [
      'from spirit.game.data_utils import EnergyCardDef',
      `from spirit.game.attributes import ${[...attrNames].sort().join(', ')}`,
      ...otherImports,
      '',
    ];
    if (helpers.length) {
      lines.push(...helpers, '');
    }
    lines.push('card = EnergyCardDef(');
    lines.push(`    guid=${pyStr(guid)},`);
    lines.push(`    key=${pyStr(setCode)},`);
    lines.push(`    name=${pyStr(resolved.name)},`);
    lines.push(`    display_name=${pyStr(resolved.name)},`);
    lines.push(`    searchable_by=${JSON.stringify(searchable)},`);
    lines.push(`    subtypes=${JSON.stringify(subtypes)},`);
    lines.push(`    collector_number=${collector},`);
    lines.push(`    set_code=${pyStr(setCode)},`);
    if (resolved.regulationMark) {
      lines.push(`    regulation_mark=${pyStr(resolved.regulationMark)},`);
    }
    lines.push(`    rarity=${rarity},`);
    lines.push(`    energy_type=${energyType},`);
    const extras: string[] = [];
    if (onAttach) extras.push(`    on_attach=${onAttach}`);
    if (energyPassive) extras.push(`    passive=${energyPassive}`);
    lines.push(`    is_special=${isSpecial ? 'True' : 'False'}${extras.length ? ',' : ''}`);
    extras.forEach((line, i) => {
      lines.push(i < extras.length - 1 ? `${line},` : line);
    });
    lines.push(')');
    return lines.join('\n') + '\n';
  }
}

/** Build a thin reprint stub. Same-set uses a local sibling; other sets use ../SET/file.py. */
export function generateReprintSource(
  draft: CardDraft,
  siblingFileName: string,
  opts?: { rarityExpr?: string; sourceSet?: string }
): string {
  const setCode = resolveSpiritSetCode(draft);
  const collector = Number(String(draft.setNumber).replace(/\D/g, '')) || 0;
  const rarity = opts?.rarityExpr || mapRarity(draft.rarity);
  const sourceSet = (opts?.sourceSet || '').trim().toUpperCase();
  const crossSet = Boolean(sourceSet && sourceSet !== setCode.toUpperCase());
  const siblingRef = crossSet ? `../${sourceSet}/${siblingFileName}` : siblingFileName;
  const args = [`               collector_number=${collector}, rarity=${rarity}`];
  if (crossSet) {
    args[args.length - 1] += ',';
    args.push(`               set_code=${pyStr(setCode)}, key=${pyStr(setCode)}`);
  }
  if (draft.regulationMark) {
    args[args.length - 1] += ',';
    args.push(`               regulation_mark=${pyStr(draft.regulationMark)}`);
  }
  args[args.length - 1] += ')';
  return [
    'from spirit.game.data_utils import reprint, sibling_card',
    'from spirit.game.attributes import Rarities',
    '',
    `card = reprint(sibling_card(__file__, ${pyStr(siblingRef)}),`,
    ...args,
    '',
  ].join('\n');
}

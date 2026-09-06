import type {
  AttackDraft,
  CardDraft,
  EnergyShort,
  PowerDraft,
  PowerTypeName,
  StageName,
  WeaknessValue,
} from '../types';
import type { TcgDexAbility, TcgDexAttack, TcgDexCard } from './client';
import { spiritSetCodeFromCatalogId } from '../generator/setMapping';
import { stripEnergyText, stripTrainerReminders } from '../trainerReminders';

function uid(prefix: string): string {
  return `${prefix}-${Math.random().toString(36).slice(2, 9)}`;
}

function toPascalCase(str: string): string {
  return str
    .replace(/[^a-zA-Z0-9 ]/g, ' ')
    .split(/\s+/)
    .filter(Boolean)
    .map(w => w.charAt(0).toUpperCase() + w.slice(1))
    .join('');
}

const TYPE_MAP: Record<string, EnergyShort> = {
  grass: 'G',
  fire: 'R',
  water: 'W',
  lightning: 'L',
  electric: 'L',
  psychic: 'P',
  fighting: 'F',
  darkness: 'D',
  dark: 'D',
  metal: 'M',
  steel: 'M',
  fairy: 'Y',
  dragon: 'N',
  colorless: 'C',
};

export function mapEnergyType(type: string | undefined): EnergyShort | '' {
  if (!type) return '';
  return TYPE_MAP[type.toLowerCase()] || '';
}

export function mapStage(stage: string | undefined): StageName {
  if (!stage) return 'BASIC';
  const s = stage.toLowerCase().replace(/[\s_-]+/g, '');
  if (s === 'basic') return 'BASIC';
  if (s === 'stage1') return 'STAGE_1';
  if (s === 'stage2') return 'STAGE_2';
  if (s === 'vmax') return 'VMAX';
  if (s === 'vstar') return 'VSTAR';
  if (s === 'vunion') return 'VUNION';
  if (s === 'legend') return 'LEGEND';
  if (s === 'mega') return 'MEGA';
  if (s === 'break') return 'BREAK';
  if (s === 'levelup' || s === 'lvx' || s === 'lv.x') return 'LV_X';
  if (s === 'restored') return 'RESTORED';
  return 'BASIC';
}

export function mapPowerType(type: string | undefined): PowerTypeName {
  if (!type) return 'ABILITY';
  const t = type.toLowerCase().replace(/[éÉ]/g, 'e').replace(/[\s_-]+/g, '');
  if (t.includes('pokepower')) return 'POKEPOWER';
  if (t.includes('pokebody')) return 'POKEBODY';
  if (t.includes('pokemonpower')) return 'POKEMON_POWER';
  if (t.includes('ancienttrait')) return 'ANCIENT_TRAIT';
  if (t.includes('ability')) return 'ABILITY';
  return 'ABILITY';
}

function parseDamage(raw: string | number | undefined): {
  damage: string;
  damageCalculation: '' | '+' | 'x' | '-';
} {
  if (raw === undefined || raw === null || raw === '') {
    return { damage: '0', damageCalculation: '' };
  }
  const s = String(raw).trim();
  if (/^\d+\+$/.test(s)) {
    return { damage: s.slice(0, -1), damageCalculation: '+' };
  }
  if (/^\d+[x×]$/i.test(s)) {
    return { damage: s.slice(0, -1), damageCalculation: 'x' };
  }
  if (/^\d+-$/.test(s)) {
    return { damage: s.slice(0, -1), damageCalculation: '-' };
  }
  const n = Number(s);
  return { damage: Number.isFinite(n) ? String(n) : '0', damageCalculation: '' };
}

function mapCost(cost: string[] | undefined): string {
  if (!cost || cost.length === 0) return '';
  return cost.map(c => mapEnergyType(c) || 'C').join('');
}

function mapWeaknessValue(value: string | undefined): WeaknessValue {
  if (!value) return 'x2';
  const v = value.trim().toLowerCase();
  if (v === 'x2' || v === '×2' || v === '*2') return 'x2';
  if (v.includes('20') || v === '+20') return '+20';
  if (v.includes('30') || v === '+30') return '+30';
  return 'x2';
}

/** SV Mega Evolution Pokémon ex ("Mega Lucario ex"), not XY-era "M Lucario-EX". */
export function isSvMegaCard(card: {
  name?: string;
  stage?: string;
  suffix?: string;
}): boolean {
  const name = card.name || '';
  const stage = (card.stage || '').toLowerCase();
  const suffix = card.suffix || '';
  const hasMega = stage === 'mega' || /\bmega\b/i.test(name);
  const hasSvEx = suffix === 'ex' || /(^|[\s])ex($|[\s])/.test(name);
  return hasMega && hasSvEx;
}

function mapTags(card: TcgDexCard): string {
  const tags: string[] = [];
  const name = (card.name || '').toLowerCase();
  const suffix = (card.suffix || '').toLowerCase();
  const stage = (card.stage || '').toLowerCase();
  const svMega = isSvMegaCard(card);

  if (svMega) {
    tags.push('POKEMON_SV_MEGA');
  } else if (suffix === 'ex' || /\bex\b/i.test(card.name) || name.endsWith(' ex')) {
    tags.push('POKEMON_ex');
  }
  if (suffix === 'gx' || name.includes('-gx') || name.endsWith(' gx')) tags.push('POKEMON_GX');
  if (suffix === 'v' || /(^|\s)v$/i.test(card.name)) tags.push('POKEMON_V');
  if (stage === 'vmax' || name.includes('vmax')) tags.push('POKEMON_VMAX');
  if (stage === 'vstar' || name.includes('vstar')) tags.push('POKEMON_VSTAR');
  if (stage === 'mega' && !svMega) tags.push('MEGA');
  if (/\blv\.?x\b/i.test(card.name) || stage.includes('level')) tags.push('POKEMON_LV_X');

  return [...new Set(tags)].join(', ');
}

function mapAttack(a: TcgDexAttack): AttackDraft {
  const { damage, damageCalculation } = parseDamage(a.damage);
  return {
    id: uid('atk'),
    enabled: true,
    name: a.name || '',
    cost: mapCost(a.cost),
    damage,
    damageCalculation,
    text: a.effect || '',
    selectedPrefabs: [],
  };
}

function mapAbility(a: TcgDexAbility): PowerDraft {
  const powerType = mapPowerType(a.type);
  const normalizedType = (a.type || '').toLowerCase();
  const isPassive = normalizedType.includes('body') || normalizedType.includes('ancient trait');
  return {
    id: uid('pwr'),
    name: a.name || '',
    powerType,
    text: a.effect || '',
    useWhenInPlay: !isPassive,
    useFromHand: false,
    useFromHandToBench: false,
    useFromDiscard: false,
    exemptFromAbilityLock: false,
    exemptFromInitialize: false,
    abilityLock: false,
    barrage: false,
    knocksOutSelf: false,
    isFossil: false,
    selectedPrefabs: [],
  };
}

function setAbbreviation(card: TcgDexCard): string {
  const official = card.set?.abbreviations?.official;
  if (official) return official.toUpperCase();
  if (card.set?.tcgOnline) return String(card.set.tcgOnline).toUpperCase();
  return (card.set?.id || '').toUpperCase();
}

function mapTrainerType(
  trainerType: string | undefined
): CardDraft['trainerType'] {
  const t = (trainerType || '').toLowerCase();
  if (t.includes('supporter')) return 'SUPPORTER';
  if (t.includes('stadium')) return 'STADIUM';
  if (t.includes('tool')) return 'TOOL';
  return 'ITEM';
}

function subtypesFromCard(card: TcgDexCard): string[] {
  const out: string[] = [];
  const stage = card.stage || '';
  const svMega = isSvMegaCard(card);
  if (stage) {
    if (/stage\s*2/i.test(stage)) out.push('Stage 2');
    else if (/stage\s*1/i.test(stage)) out.push('Stage 1');
    else if (/vmax/i.test(stage)) out.push('VMAX');
    else if (/vstar/i.test(stage)) out.push('VSTAR');
    else if (/basic/i.test(stage)) out.push('Basic');
    else if (/^mega$/i.test(stage) || svMega) out.push(card.evolveFrom ? 'Stage 1' : 'Basic');
    else out.push(stage);
  }
  if (card.suffix) out.push(card.suffix);
  if (svMega) {
    if (card.evolveFrom) {
      const filtered = out.filter(s => s !== 'Basic');
      out.length = 0;
      out.push(...filtered);
      if (!out.includes('Stage 1')) out.unshift('Stage 1');
    } else {
      const filtered = out.filter(s => s !== 'Stage 1');
      out.length = 0;
      out.push(...filtered);
      if (!out.includes('Basic')) out.unshift('Basic');
    }
    out.push('SV_Mega');
  } else if (/^mega$/i.test(stage)) {
    out.push('MEGA');
  }
  if (card.trainerType) out.push(card.trainerType);
  if (card.energyType) out.push(card.energyType);
  if (card.category === 'Pokemon' && out.length === 0) out.push('Basic');
  return [...new Set(out.filter(Boolean))];
}

/**
 * Convert a catalog card payload into a CardDraft for the generator form.
 */
export function mapTcgDexCardToDraft(card: TcgDexCard): CardDraft {
  const category = (card.category || '').toLowerCase();
  const name = card.name || '';
  const set = setAbbreviation(card);
  const setNumber = String(card.localId || '');
  const catalogId = card.id || '';
  const spiritSetCode = spiritSetCodeFromCatalogId(catalogId);

  const base: CardDraft = {
    className: toPascalCase(name),
    extends: 'PokemonCard',
    stage: 'BASIC',
    evolvesFrom: '',
    tags: '',
    hp: '0',
    cardType: 'C',
    weaknessType: '',
    weaknessValue: 'x2',
    resistanceType: '',
    resistanceValue: '-20',
    retreat: '',
    hasPowers: false,
    hasAttacks: true,
    powers: [],
    attacks: [],
    regulationMark: card.regulationMark || '',
    set,
    setNumber,
    name,
    catalogId,
    spiritSetCode,
    rarity: card.rarity || '',
    subtypes: subtypesFromCard(card),
    imageUrl: card.image || '',
    familyId: '',
    trainerType: 'ITEM',
    trainerText: '',
    trainerPrefabs: [],
    energyType: 'BASIC',
    provides: 'C',
    blendedEnergies: '',
    blendedEnergyCount: '1',
    energyText: '',
    energyPrefabs: [],
  };

  if (category === 'trainer') {
    base.extends = 'TrainerCard';
    base.hasAttacks = false;
    base.hasPowers = false;
    base.trainerType = mapTrainerType(card.trainerType);
    base.trainerText = stripTrainerReminders(card.effect || '');
    return base;
  }

  if (category === 'energy') {
    base.extends = 'EnergyCard';
    base.hasAttacks = false;
    base.hasPowers = false;
    base.energyType = (card.energyType || '').toLowerCase().includes('special')
      ? 'SPECIAL'
      : 'BASIC';
    const words = name.replace(/\s*energy$/i, '').trim().split(/\s+/);
    const fromName = mapEnergyType(words[words.length - 1]);
    const fromText = (card.effect || '').match(/provides\s+(\w+)\s+energy/i);
    base.provides = fromName || mapEnergyType(fromText?.[1]) || 'C';
    base.energyText = stripEnergyText(card.effect || '');
    base.energyPrefabs = [];
    return base;
  }

  base.extends = 'PokemonCard';
  base.stage = mapStage(card.stage);
  base.evolvesFrom = card.evolveFrom || '';
  if (isSvMegaCard(card) || base.stage === 'MEGA') {
    base.stage = base.evolvesFrom ? 'STAGE_1' : 'BASIC';
  }
  base.tags = mapTags(card);
  base.hp = String(card.hp ?? 0);
  base.cardType = mapEnergyType(card.types?.[0]) || 'C';

  const weak = card.weaknesses?.[0];
  if (weak) {
    base.weaknessType = mapEnergyType(weak.type) || '';
    base.weaknessValue = mapWeaknessValue(weak.value);
  }

  const res = card.resistances?.[0];
  if (res) {
    base.resistanceType = mapEnergyType(res.type) || '';
    const rv = (res.value || '-20').replace(/[^\d-]/g, '');
    base.resistanceValue = rv || '-20';
  }

  const retreatCount = typeof card.retreat === 'number' ? card.retreat : 0;
  base.retreat = 'C'.repeat(Math.max(0, retreatCount));

  const attacks = (card.attacks || []).map(mapAttack);
  const powers = (card.abilities || []).map(mapAbility);

  base.hasAttacks = attacks.length > 0;
  base.hasPowers = powers.length > 0;
  base.attacks = attacks.length > 0 ? attacks : [];
  base.powers = powers.length > 0 ? powers : [];

  return base;
}

export interface BrowseSourceMeta {
  tcgDexId: string;
  imageUrl?: string;
  setName?: string;
  rarity?: string;
  region?: 'en' | 'jp';
  unofficialTranslation?: boolean;
  intPrintHint?: string;
}

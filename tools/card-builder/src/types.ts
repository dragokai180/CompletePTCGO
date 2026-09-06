export type CardBase = 'PokemonCard' | 'TrainerCard' | 'EnergyCard';
export type EffectKind = 'attack' | 'power' | 'trainer' | 'energy';

export type EnergyShort =
  | 'G'
  | 'R'
  | 'W'
  | 'L'
  | 'P'
  | 'F'
  | 'D'
  | 'M'
  | 'Y'
  | 'N'
  | 'C'
  | 'A';

export const ENERGY_SHORTS: EnergyShort[] = [
  'G',
  'R',
  'W',
  'L',
  'P',
  'F',
  'D',
  'M',
  'Y',
  'N',
  'C',
];

export const ENERGY_LABELS: Record<EnergyShort, string> = {
  G: 'Grass (G)',
  R: 'Fire (R)',
  W: 'Water (W)',
  L: 'Lightning (L)',
  P: 'Psychic (P)',
  F: 'Fighting (F)',
  D: 'Dark (D)',
  M: 'Metal (M)',
  Y: 'Fairy (Y)',
  N: 'Dragon (N)',
  C: 'Colorless (C)',
  A: 'Any type (A)',
};

export const STAGES = [
  'BASIC',
  'STAGE_1',
  'STAGE_2',
  'VMAX',
  'VSTAR',
  'VUNION',
  'LEGEND',
  'MEGA',
  'BREAK',
  'LV_X',
  'RESTORED',
  'NONE',
] as const;

export type StageName = (typeof STAGES)[number];

export const POWER_TYPES = [
  'ABILITY',
  'POKEPOWER',
  'POKEBODY',
  'POKEMON_POWER',
  'ANCIENT_TRAIT',
  'BABY_RULE',
  'HELD_ITEM',
  'VUNION_ASSEMBLY',
  'LEGEND_ASSEMBLY',
  'TRAINER_ABILITY',
  'HOLONS_SPECIAL_ENERGY_EFFECT',
  'ENERGY_ABILITY',
  'MEGA_EVOLUTION_RULE',
  'LV_X_RULE',
  'BREAK_RULE',
  'ARCEUS_RULE',
] as const;

export type PowerTypeName = (typeof POWER_TYPES)[number];

export type WeaknessValue = 'x2' | '+20' | '+30';

export type PrefabScope = EffectKind | 'both';

export interface PrefabParamDef {
  key: string;
  label: string;
  type: 'number' | 'string' | 'energy' | 'boolean';
  defaultValue?: string | number | boolean;
}

export interface PrefabDefinition {
  id: string;
  name: string;
  description: string;
  exampleTexts: string[];
  scope: PrefabScope;
  importFrom: string;
  importNames: string[];
  /** Extra imports needed beyond the prefab itself (e.g. MarkerConstants). */
  extraImports?: string[];
  params: PrefabParamDef[];
  /** Patterns tried against normalized effect text. Capture groups map to param keys via paramCaptures. */
  patterns: RegExp[];
  /** Maps capture group index (1-based) to param key. */
  paramCaptures?: Record<number, string>;
  /**
   * Generate the body lines inside the WAS_ATTACK_USED / WAS_POWER_USED block.
   * Return true if the last statement should be returned.
   */
  generateCall: (params: Record<string, string>, ctx: PrefabGenContext) => PrefabCallResult;
  /** Optional companion lines outside the attack/power block (markers, cleanup). */
  generateCompanions?: (params: Record<string, string>, ctx: PrefabGenContext) => string[];
}

export interface PrefabGenContext {
  kind: EffectKind;
  index: number;
  attackName?: string;
  powerName?: string;
}

export interface PrefabImport {
  module: string;
  names: string[];
}

export interface PrefabCallResult {
  /** Display / legacy lines (Spirit uses effectExpr). */
  lines: string[];
  /** Spirit factory expression for effect=… */
  effectExpr?: string;
  /** Optional Ability activation enum expression. */
  activation?: string;
  /** Ability.trigger expression, e.g. Triggers.ON_EVOLVE. */
  trigger?: string;
  /** Ability.passive expression. */
  passive?: string;
  /** Ability.shared_once_per_turn label. */
  sharedOncePerTurn?: string;
  /** Attack.locks_next_turn=True */
  locksNextTurn?: boolean;
  /** Trainer play-condition expression. */
  condition?: string;
  /** Module-level helper defs to emit above `card =`. */
  helpers?: string[];
  /** Named imports required by effectExpr / activation. */
  imports?: PrefabImport[];
  returns?: boolean;
}

export interface MatchedPrefab {
  prefab: PrefabDefinition;
  params: Record<string, string>;
  matchedText: string;
}

export interface SelectedPrefab {
  id: string;
  prefabId: string;
  params: Record<string, string>;
  /** How it was added: auto-matched from text, or manually picked. */
  source: 'matched' | 'manual';
}

export interface AttackDraft {
  id: string;
  enabled: boolean;
  name: string;
  cost: string;
  damage: string;
  damageCalculation: '' | '+' | 'x' | '-';
  text: string;
  selectedPrefabs: SelectedPrefab[];
  serverEffect?: ServerEffect;
  matchError?: string;
}

export interface PowerDraft {
  id: string;
  name: string;
  powerType: PowerTypeName;
  text: string;
  useWhenInPlay: boolean;
  useFromHand: boolean;
  useFromHandToBench: boolean;
  useFromDiscard: boolean;
  exemptFromAbilityLock: boolean;
  exemptFromInitialize: boolean;
  abilityLock: boolean;
  barrage: boolean;
  knocksOutSelf: boolean;
  isFossil: boolean;
  selectedPrefabs: SelectedPrefab[];
  serverEffect?: ServerEffect;
  matchError?: string;
}

export interface ServerEffect {
  source: string;
  effectText: string;
  /** Kept for compatibility with older server-card-effects payloads. */
  attackText?: string;
  kind: EffectKind;
  body: string[];
  imports: string[];
  similarity: number;
  bodyMode?: 'branch' | 'full';
  helpers?: string[];
  /** Play-condition expression, e.g. hand_size_at_least(3). */
  condition?: string;
  /** Ability.trigger expression copied from a similar script. */
  trigger?: string;
  /** Ability.activation expression copied from a similar script. */
  activation?: string;
  /** Ability.passive expression copied from a similar script. */
  passive?: string;
  /** Ability.shared_once_per_turn label. */
  sharedOncePerTurn?: string;
  /** Attack.locks_next_turn. */
  locksNextTurn?: boolean;
  /** Scripts / factories this effect was assembled from. */
  sources?: string[];
}

export interface ReprintCandidate {
  className: string;
  name: string;
  set: string;
  setNumber: string;
  fullName: string;
  sourcePath: string;
  /** Basename of the sibling script, e.g. Torchic_22.py */
  fileName?: string;
  category?: 'pokemon' | 'trainer' | 'energy';
  /** Gameplay fingerprint for Pokémon; omitted for trainers/energy. */
  reprintIdentity?: string | null;
}

export interface CardDraft {
  className: string;
  extends: CardBase;
  // Pokemon
  stage: StageName;
  evolvesFrom: string;
  tags: string;
  hp: string;
  cardType: EnergyShort;
  weaknessType: '' | EnergyShort;
  weaknessValue: WeaknessValue;
  resistanceType: '' | EnergyShort;
  resistanceValue: string;
  retreat: string;
  hasPowers: boolean;
  hasAttacks: boolean;
  powers: PowerDraft[];
  attacks: AttackDraft[];
  // Shared meta
  regulationMark: string;
  set: string;
  setNumber: string;
  name: string;
  /** pokemon-tcg-data id, e.g. sv9-22 */
  catalogId: string;
  /** Spirit folder code, e.g. SV09 */
  spiritSetCode: string;
  rarity: string;
  subtypes: string[];
  imageUrl: string;
  familyId: string;
  // Trainer
  trainerType: 'ITEM' | 'SUPPORTER' | 'STADIUM' | 'TOOL';
  trainerText: string;
  trainerPrefabs: SelectedPrefab[];
  trainerServerEffect?: ServerEffect;
  // Energy
  energyType: 'BASIC' | 'SPECIAL';
  provides: string;
  blendedEnergies: string;
  blendedEnergyCount: string;
  energyText: string;
  energyPrefabs: SelectedPrefab[];
  energyServerEffect?: ServerEffect;
}

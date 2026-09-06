import { effectFnName } from '../generator/effectFnName';
import type { PrefabDefinition, PrefabImport } from '../types';

const ATTACKS = 'spirit.game.card_effects.attacks_common';
const SUPPORT = 'spirit.game.card_effects.support_common';
const TRAINERS = 'spirit.game.card_effects.trainers';
const DATA = 'spirit.game.data_utils';
const ATTR = 'spirit.game.attributes';
const PASSIVES = 'spirit.game.card_effects.passives_common';
const POKEMON = 'spirit.game.card_effects.pokemon';

const TYPE_ENUM_NAME: Record<string, string> = {
  grass: 'GRASS',
  fire: 'FIRE',
  water: 'WATER',
  lightning: 'LIGHTNING',
  electric: 'LIGHTNING',
  psychic: 'PSYCHIC',
  fighting: 'FIGHTING',
  darkness: 'DARKNESS',
  dark: 'DARKNESS',
  metal: 'METAL',
  steel: 'METAL',
  fairy: 'FAIRY',
  dragon: 'DRAGON',
  colorless: 'COLORLESS',
};

function typeEnumId(name: string): string {
  return TYPE_ENUM_NAME[name.toLowerCase()] || name.toUpperCase();
}

function titleCase(name: string): string {
  return name ? name.charAt(0).toUpperCase() + name.slice(1).toLowerCase() : '';
}

function pascalIdent(name: string): string {
  return name
    .replace(/[^a-zA-Z0-9]+/g, ' ')
    .split(' ')
    .filter(Boolean)
    .map(titleCase)
    .join('');
}

function num(params: Record<string, string>, key: string, fallback = '0'): string {
  const raw = params[key];
  if (raw === undefined || raw === '') return fallback;
  return String(Number(raw));
}

function imp(module: string, ...names: string[]): PrefabImport[] {
  return [{ module, names }];
}

function effect(
  expr: string,
  imports: PrefabImport[],
  extras: Partial<PrefabDefinition['generateCall'] extends never ? never : ReturnType<PrefabDefinition['generateCall']>> = {}
) {
  return {
    lines: [expr],
    effectExpr: expr,
    imports,
    ...extras,
  };
}

/** Catalog of Spirit factory prefabs the builder may emit. */
export const PREFAB_CATALOG: PrefabDefinition[] = [
  // ── Ability activation marker ───────────────────────────────────────────
  {
    id: 'USE_ABILITY_ONCE_PER_TURN',
    name: 'ONCE_PER_TURN',
    description: 'Ability usable once per turn.',
    exampleTexts: ['Once during your turn…'],
    scope: 'power',
    importFrom: DATA,
    importNames: ['Activations'],
    params: [],
    patterns: [/^once during your turn\.?$/i],
    generateCall: () => ({
      lines: ['activation=Activations.ONCE_PER_TURN'],
      activation: 'Activations.ONCE_PER_TURN',
      imports: imp(DATA, 'Activations'),
    }),
  },
  {
    id: 'ON_EVOLVE',
    name: 'Triggers.ON_EVOLVE',
    description: 'Fires when this Pokémon is played from hand to evolve.',
    exampleTexts: [
      'When you play this Pokémon from your hand to evolve 1 of your Pokémon, you may use this Ability.',
    ],
    scope: 'power',
    importFrom: DATA,
    importNames: ['Triggers'],
    params: [],
    patterns: [],
    generateCall: () => ({
      lines: ['trigger=Triggers.ON_EVOLVE'],
      trigger: 'Triggers.ON_EVOLVE',
      imports: imp(DATA, 'Triggers'),
    }),
  },
  {
    id: 'ON_PLAY',
    name: 'Triggers.ON_PLAY',
    description: 'Fires when this Pokémon is played from hand onto the Bench.',
    exampleTexts: [
      'When you play this Pokémon from your hand onto your Bench, you may use this Ability.',
    ],
    scope: 'power',
    importFrom: DATA,
    importNames: ['Triggers'],
    params: [],
    patterns: [],
    generateCall: () => ({
      lines: ['trigger=Triggers.ON_PLAY'],
      trigger: 'Triggers.ON_PLAY',
      imports: imp(DATA, 'Triggers'),
    }),
  },
  {
    id: 'IN_ACTIVE_SPOT',
    name: 'in_active_spot',
    description: 'Ability requires this Pokémon to be in the Active Spot.',
    exampleTexts: ['If this Pokémon is in the Active Spot, you may use this Ability.'],
    scope: 'power',
    importFrom: POKEMON,
    importNames: ['in_active_spot'],
    params: [],
    patterns: [],
    generateCall: () => ({
      lines: ['condition=in_active_spot'],
      condition: 'in_active_spot',
      imports: imp(POKEMON, 'in_active_spot'),
    }),
  },
  {
    id: 'SHARED_ONCE_PER_TURN',
    name: 'shared_once_per_turn',
    description: "You can't use more than 1 copy of this Ability each turn.",
    exampleTexts: ["You can't use more than 1 Run Errand Ability each turn."],
    scope: 'power',
    importFrom: '',
    importNames: [],
    params: [{ key: 'name', label: 'Ability name', type: 'string' }],
    patterns: [],
    generateCall: (params, ctx) => ({
      lines: [],
      sharedOncePerTurn: params.name || ctx.powerName || '',
      imports: [],
    }),
  },

  // ── Drawing ─────────────────────────────────────────────────────────────
  {
    id: 'DRAW_CARDS',
    name: 'draw_attack / draw',
    description: 'Draw X cards. Attacks use draw_attack; Abilities emit a helper.',
    exampleTexts: ['Draw a card.', 'Draw 2 cards.', 'Draw 3 cards.'],
    scope: 'both',
    importFrom: SUPPORT,
    importNames: ['draw_attack'],
    params: [{ key: 'count', label: 'Cards', type: 'number', defaultValue: 1 }],
    patterns: [/^draw a card\.?$/i, /^draw (\d+) cards?\.?$/i],
    paramCaptures: { 1: 'count' },
    generateCall: (params, ctx) => {
      const count = params.count === undefined || params.count === '' ? '1' : num(params, 'count', '1');
      if (ctx.kind === 'power') {
        const fn = effectFnName(ctx.powerName || 'draw');
        const n = Number(count);
        const prompt = n === 1 ? 'Draw a card?' : `Draw ${n} cards?`;
        const body =
          params.may === 'true'
            ? `    if await ctx.ask_yes_no(${JSON.stringify(prompt)}):\n        await ctx.draw_cards(${count})\n`
            : `    await ctx.draw_cards(${count})\n`;
        return {
          lines: [fn],
          effectExpr: fn,
          helpers: [`async def ${fn}(ctx):\n${body}`],
          imports: [],
        };
      }
      return effect(`draw_attack(${count})`, imp(SUPPORT, 'draw_attack'));
    },
  },
  {
    id: 'DRAW_UNTIL_HAND',
    name: 'draw_until_effect',
    description: 'Draw until you have X cards in hand.',
    exampleTexts: ['Draw cards until you have 6 cards in your hand.'],
    scope: 'both',
    importFrom: SUPPORT,
    importNames: ['draw_until_effect'],
    params: [{ key: 'count', label: 'Hand size', type: 'number', defaultValue: 7 }],
    patterns: [
      /^draw(?: cards)? until you have (\d+) cards? in your hand\.?$/i,
      /^draw until you have (\d+) cards? in your hand\.?$/i,
    ],
    paramCaptures: { 1: 'count' },
    generateCall: (params) => {
      const n = num(params, 'count', '7');
      return effect(`draw_until_effect(${n})`, imp(SUPPORT, 'draw_until_effect'));
    },
  },
  {
    id: 'DISCARD_THEN_DRAW',
    name: 'discard_then_draw',
    description: 'Discard X cards, then draw Y.',
    exampleTexts: ['Discard a card from your hand. If you do, draw 2 cards.'],
    scope: 'both',
    importFrom: SUPPORT,
    importNames: ['discard_then_draw'],
    params: [
      { key: 'discard', label: 'Discard', type: 'number', defaultValue: 1 },
      { key: 'draw', label: 'Draw', type: 'number', defaultValue: 2 },
    ],
    patterns: [
      /^discard (?:a|1) card(?: from your hand)?\.?\s*(?:if you do,?\s*)?draw (\d+) cards?\.?$/i,
      /^discard (\d+) cards?(?: from your hand)?\.?\s*(?:if you do,?\s*)?draw (\d+) cards?\.?$/i,
    ],
    paramCaptures: { 1: 'draw' },
    generateCall: (params) => {
      const discard = params.discard && params.discard !== '' ? num(params, 'discard', '1') : '1';
      const draw = num(params, 'draw', '2');
      return effect(
        `discard_then_draw(${discard}, ${draw}, optional=False)`,
        imp(SUPPORT, 'discard_then_draw'),
      );
    },
  },

  // ── Special conditions ──────────────────────────────────────────────────
  {
    id: 'ACTIVE_NOW_PARALYZED',
    name: 'condition_attack(PARALYZED)',
    description: "Opponent's Active is now Paralyzed.",
    exampleTexts: ["Your opponent's Active Pokémon is now Paralyzed."],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['condition_attack'],
    params: [],
    patterns: [/^your opponent'?s active pok[eé]mon is now paralyzed\.?$/i],
    generateCall: () =>
      effect(
        'condition_attack(SpecialConditions.PARALYZED)',
        [...imp(ATTACKS, 'condition_attack'), ...imp(ATTR, 'SpecialConditions')],
      ),
  },
  {
    id: 'ACTIVE_NOW_ASLEEP',
    name: 'condition_attack(ASLEEP)',
    description: "Opponent's Active is now Asleep.",
    exampleTexts: ["Your opponent's Active Pokémon is now Asleep."],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['condition_attack'],
    params: [],
    patterns: [/^your opponent'?s active pok[eé]mon is now asleep\.?$/i],
    generateCall: () =>
      effect(
        'condition_attack(SpecialConditions.ASLEEP)',
        [...imp(ATTACKS, 'condition_attack'), ...imp(ATTR, 'SpecialConditions')],
      ),
  },
  {
    id: 'ACTIVE_NOW_CONFUSED',
    name: 'condition_attack(CONFUSED)',
    description: "Opponent's Active is now Confused.",
    exampleTexts: ["Your opponent's Active Pokémon is now Confused."],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['condition_attack'],
    params: [],
    patterns: [/^your opponent'?s active pok[eé]mon is now confused\.?$/i],
    generateCall: () =>
      effect(
        'condition_attack(SpecialConditions.CONFUSED)',
        [...imp(ATTACKS, 'condition_attack'), ...imp(ATTR, 'SpecialConditions')],
      ),
  },
  {
    id: 'ACTIVE_NOW_POISONED',
    name: 'condition_attack(POISONED)',
    description: "Opponent's Active is now Poisoned.",
    exampleTexts: ["Your opponent's Active Pokémon is now Poisoned."],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['condition_attack'],
    params: [],
    patterns: [/^your opponent'?s active pok[eé]mon is now poisoned\.?$/i],
    generateCall: () =>
      effect(
        'condition_attack(SpecialConditions.POISONED)',
        [...imp(ATTACKS, 'condition_attack'), ...imp(ATTR, 'SpecialConditions')],
      ),
  },
  {
    id: 'ACTIVE_NOW_BURNED',
    name: 'condition_attack(BURNED)',
    description: "Opponent's Active is now Burned.",
    exampleTexts: ["Your opponent's Active Pokémon is now Burned."],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['condition_attack'],
    params: [],
    patterns: [/^your opponent'?s active pok[eé]mon is now burned\.?$/i],
    generateCall: () =>
      effect(
        'condition_attack(SpecialConditions.BURNED)',
        [...imp(ATTACKS, 'condition_attack'), ...imp(ATTR, 'SpecialConditions')],
      ),
  },
  {
    id: 'FLIP_HEADS_PARALYZED',
    name: 'condition_attack(PARALYZED, flip)',
    description: 'Flip: if heads, Paralyzed.',
    exampleTexts: ['Flip a coin. If heads, your opponent\'s Active Pokémon is now Paralyzed.'],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['condition_attack'],
    params: [],
    patterns: [
      /^flip a coin\.?\s*if heads,?\s*your opponent'?s active pok[eé]mon is now paralyzed\.?$/i,
    ],
    generateCall: () =>
      effect(
        'condition_attack(SpecialConditions.PARALYZED, flip=True)',
        [...imp(ATTACKS, 'condition_attack'), ...imp(ATTR, 'SpecialConditions')],
      ),
  },
  {
    id: 'FLIP_HEADS_ASLEEP',
    name: 'condition_attack(ASLEEP, flip)',
    description: 'Flip: if heads, Asleep.',
    exampleTexts: ['Flip a coin. If heads, your opponent\'s Active Pokémon is now Asleep.'],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['condition_attack'],
    params: [],
    patterns: [
      /^flip a coin\.?\s*if heads,?\s*your opponent'?s active pok[eé]mon is now asleep\.?$/i,
    ],
    generateCall: () =>
      effect(
        'condition_attack(SpecialConditions.ASLEEP, flip=True)',
        [...imp(ATTACKS, 'condition_attack'), ...imp(ATTR, 'SpecialConditions')],
      ),
  },
  {
    id: 'FLIP_HEADS_POISONED',
    name: 'condition_attack(POISONED, flip)',
    description: 'Flip: if heads, Poisoned.',
    exampleTexts: ['Flip a coin. If heads, your opponent\'s Active Pokémon is now Poisoned.'],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['condition_attack'],
    params: [],
    patterns: [
      /^flip a coin\.?\s*if heads,?\s*your opponent'?s active pok[eé]mon is now poisoned\.?$/i,
    ],
    generateCall: () =>
      effect(
        'condition_attack(SpecialConditions.POISONED, flip=True)',
        [...imp(ATTACKS, 'condition_attack'), ...imp(ATTR, 'SpecialConditions')],
      ),
  },
  {
    id: 'FLIP_HEADS_BURNED',
    name: 'condition_attack(BURNED, flip)',
    description: 'Flip: if heads, Burned.',
    exampleTexts: ['Flip a coin. If heads, your opponent\'s Active Pokémon is now Burned.'],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['condition_attack'],
    params: [],
    patterns: [
      /^flip a coin\.?\s*if heads,?\s*your opponent'?s active pok[eé]mon is now burned\.?$/i,
    ],
    generateCall: () =>
      effect(
        'condition_attack(SpecialConditions.BURNED, flip=True)',
        [...imp(ATTACKS, 'condition_attack'), ...imp(ATTR, 'SpecialConditions')],
      ),
  },
  {
    id: 'FLIP_HEADS_CONFUSED',
    name: 'condition_attack(CONFUSED, flip)',
    description: 'Flip: if heads, Confused.',
    exampleTexts: ['Flip a coin. If heads, your opponent\'s Active Pokémon is now Confused.'],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['condition_attack'],
    params: [],
    patterns: [
      /^flip a coin\.?\s*if heads,?\s*your opponent'?s active pok[eé]mon is now confused\.?$/i,
    ],
    generateCall: () =>
      effect(
        'condition_attack(SpecialConditions.CONFUSED, flip=True)',
        [...imp(ATTACKS, 'condition_attack'), ...imp(ATTR, 'SpecialConditions')],
      ),
  },

  // ── Coin flip damage ────────────────────────────────────────────────────
  {
    id: 'FLIP_BONUS_DAMAGE',
    name: 'flip_bonus',
    description: 'Flip: if heads, do X more damage.',
    exampleTexts: ['Flip a coin. If heads, this attack does 30 more damage.'],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['flip_bonus'],
    params: [{ key: 'bonus', label: 'Bonus', type: 'number', defaultValue: 30 }],
    patterns: [
      /^flip a coin\.?\s*if heads,?\s*this attack does (\d+) more damage\.?$/i,
    ],
    paramCaptures: { 1: 'bonus' },
    generateCall: (params) =>
      effect(`flip_bonus(${num(params, 'bonus', '30')})`, imp(ATTACKS, 'flip_bonus')),
  },
  {
    id: 'FLIP_UNTIL_TAILS_PER_HEADS',
    name: 'flip_damage(until_tails)',
    description: 'Flip until tails; X damage per heads.',
    exampleTexts: ['Flip a coin until you get tails. This attack does 30 damage for each heads.'],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['flip_damage'],
    params: [{ key: 'per', label: 'Per heads', type: 'number', defaultValue: 30 }],
    patterns: [
      /^flip a coin until you get tails\.?\s*this attack does (\d+) damage for each heads\.?$/i,
    ],
    paramCaptures: { 1: 'per' },
    generateCall: (params) =>
      effect(
        `flip_damage(until_tails=True, per_heads=${num(params, 'per', '30')})`,
        imp(ATTACKS, 'flip_damage'),
      ),
  },
  {
    id: 'FLIP_UNTIL_TAILS_MORE_PER_HEADS',
    name: 'flip_damage(bonus until tails)',
    description: 'Flip until tails; +X more damage per heads.',
    exampleTexts: [
      'Flip a coin until you get tails. This attack does 30 more damage for each heads.',
    ],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['flip_damage'],
    params: [{ key: 'per', label: 'Per heads', type: 'number', defaultValue: 30 }],
    patterns: [
      /^flip a coin until you get tails\.?\s*this attack does (\d+) more damage for each heads\.?$/i,
    ],
    paramCaptures: { 1: 'per' },
    generateCall: (params) =>
      effect(
        `flip_damage(until_tails=True, bonus_per_heads=${num(params, 'per', '30')})`,
        imp(ATTACKS, 'flip_damage'),
      ),
  },
  {
    id: 'FLIP_N_COINS_PER_HEADS',
    name: 'flip_damage(coins)',
    description: 'Flip N coins; X damage per heads.',
    exampleTexts: ['Flip 2 coins. This attack does 40 damage for each heads.'],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['flip_damage'],
    params: [
      { key: 'coins', label: 'Coins', type: 'number', defaultValue: 2 },
      { key: 'per', label: 'Per heads', type: 'number', defaultValue: 40 },
    ],
    patterns: [
      /^flip (\d+) coins?\.?\s*this attack does (\d+) damage for each heads\.?$/i,
    ],
    paramCaptures: { 1: 'coins', 2: 'per' },
    generateCall: (params) =>
      effect(
        `flip_damage(coins=${num(params, 'coins', '2')}, per_heads=${num(params, 'per', '40')})`,
        imp(ATTACKS, 'flip_damage'),
      ),
  },

  // ── Recoil / self damage ────────────────────────────────────────────────
  {
    id: 'RECOIL',
    name: 'recoil_attack',
    description: 'This Pokémon also does X damage to itself.',
    exampleTexts: ['This Pokémon also does 30 damage to itself.'],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['recoil_attack'],
    params: [{ key: 'amount', label: 'Self damage', type: 'number', defaultValue: 30 }],
    patterns: [
      /^this pok[eé]mon (?:also )?does (\d+) damage to itself\.?$/i,
    ],
    paramCaptures: { 1: 'amount' },
    generateCall: (params) =>
      effect(`recoil_attack(${num(params, 'amount', '30')})`, imp(ATTACKS, 'recoil_attack')),
  },

  // ── Snipe ───────────────────────────────────────────────────────────────
  {
    id: 'SNIPE_BENCH',
    name: 'snipe_attack(bench)',
    description: 'Deal X to 1 of opponent\'s Benched Pokémon.',
    exampleTexts: [
      "This attack does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
    ],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['snipe_attack'],
    params: [{ key: 'amount', label: 'Damage', type: 'number', defaultValue: 30 }],
    patterns: [
      /^this attack does (\d+) damage to 1 of your opponent'?s benched pok[eé]mon\.?(?:\s*\(don't apply weakness and resistance for benched pok[eé]mon\.\))?$/i,
    ],
    paramCaptures: { 1: 'amount' },
    generateCall: (params) =>
      effect(
        `snipe_attack(${num(params, 'amount', '30')}, pool="bench")`,
        imp(ATTACKS, 'snipe_attack'),
      ),
  },
  {
    id: 'SNIPE_BENCH_ALSO',
    name: 'snipe_attack(also_base)',
    description: 'Deal printed damage, then X to 1 of opponent\'s Benched Pokémon.',
    exampleTexts: [
      "This attack also does 50 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
    ],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['snipe_attack'],
    params: [{ key: 'amount', label: 'Bench damage', type: 'number', defaultValue: 50 }],
    patterns: [
      /^this attack also does (\d+) damage to 1 of your opponent'?s benched pok[eé]mon\.?(?:\s*\(don't apply weakness and resistance for benched pok[eé]mon\.\))?$/i,
    ],
    paramCaptures: { 1: 'amount' },
    generateCall: (params) =>
      effect(
        `snipe_attack(${num(params, 'amount', '50')}, also_base=True)`,
        imp(ATTACKS, 'snipe_attack'),
      ),
  },
  {
    id: 'SNIPE_ANY',
    name: 'snipe_attack(any)',
    description: 'Deal X to 1 of opponent\'s Pokémon.',
    exampleTexts: [
      "This attack does 30 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
    ],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['snipe_attack'],
    params: [{ key: 'amount', label: 'Damage', type: 'number', defaultValue: 30 }],
    patterns: [
      /^this attack does (\d+) damage to 1 of your opponent'?s pok[eé]mon\.?(?:\s*\(don't apply weakness and resistance for benched pok[eé]mon\.\))?$/i,
    ],
    paramCaptures: { 1: 'amount' },
    generateCall: (params) =>
      effect(
        `snipe_attack(${num(params, 'amount', '30')}, pool="any")`,
        imp(ATTACKS, 'snipe_attack'),
      ),
  },

  // ── Heal ────────────────────────────────────────────────────────────────
  {
    id: 'HEAL_SELF',
    name: 'heal_attack',
    description: 'Heal X damage from this Pokémon.',
    exampleTexts: ['Heal 30 damage from this Pokémon.'],
    scope: 'attack',
    importFrom: SUPPORT,
    importNames: ['heal_attack'],
    params: [{ key: 'amount', label: 'Heal', type: 'number', defaultValue: 30 }],
    patterns: [/^heal (\d+) damage from this pok[eé]mon\.?$/i],
    paramCaptures: { 1: 'amount' },
    generateCall: (params) =>
      effect(`heal_attack(${num(params, 'amount', '30')})`, imp(SUPPORT, 'heal_attack')),
  },
  {
    id: 'HEAL_ITEM',
    name: 'heal_item',
    description: 'Heal X from 1 of your Pokémon.',
    exampleTexts: ['Heal 30 damage from 1 of your Pokémon.'],
    scope: 'trainer',
    importFrom: SUPPORT,
    importNames: ['heal_item'],
    params: [{ key: 'amount', label: 'Heal', type: 'number', defaultValue: 30 }],
    patterns: [
      /^heal (\d+) damage from 1 of your pok[eé]mon\.?$/i,
    ],
    paramCaptures: { 1: 'amount' },
    generateCall: (params) =>
      effect(
        `heal_item(${num(params, 'amount', '30')})`,
        imp(SUPPORT, 'heal_item', 'requires_damaged_pokemon'),
        { condition: 'requires_damaged_pokemon()' },
      ),
  },
  {
    id: 'HEAL_ACTIVE',
    name: 'heal_item(active)',
    description: 'Heal X from your Active Pokémon.',
    exampleTexts: ['Heal 70 damage from your Active Pokémon.'],
    scope: 'trainer',
    importFrom: SUPPORT,
    importNames: ['heal_item', 'requires_damaged_pokemon'],
    params: [{ key: 'amount', label: 'Heal', type: 'number', defaultValue: 70 }],
    patterns: [/^heal (\d+) damage from your active pok[eé]mon\.?$/i],
    paramCaptures: { 1: 'amount' },
    generateCall: (params) =>
      effect(
        `heal_item(${num(params, 'amount', '70')}, scope="active")`,
        imp(SUPPORT, 'heal_item', 'requires_damaged_pokemon'),
        { condition: 'requires_damaged_pokemon()' },
      ),
  },
  {
    id: 'HEAL_ACTIVE_WITH_ENERGY',
    name: 'heal Active with N Energy',
    description: 'Heal X from your Active Pokémon that has N or more Energy attached.',
    exampleTexts: ['Heal 80 damage from your Active Pokémon that has 3 or more Energy attached.'],
    scope: 'trainer',
    importFrom: SUPPORT,
    importNames: ['heal_item', 'requires_damaged_active_with_energy'],
    params: [
      { key: 'amount', label: 'Heal', type: 'number', defaultValue: 80 },
      { key: 'energy', label: 'Energy', type: 'number', defaultValue: 3 },
    ],
    patterns: [
      /^heal (\d+) damage from your active pok[eé]mon that has (\d+) or more energy attached\.?$/i,
    ],
    paramCaptures: { 1: 'amount', 2: 'energy' },
    generateCall: (params) =>
      effect(
        `heal_item(${num(params, 'amount', '80')}, scope="active")`,
        imp(SUPPORT, 'heal_item', 'requires_damaged_active_with_energy'),
        { condition: `requires_damaged_active_with_energy(${num(params, 'energy', '3')})` },
      ),
  },
  {
    id: 'HEAL_TYPED_POKEMON',
    name: 'heal 1 of your typed Pokémon',
    description: 'Heal X from 1 of your [Type] Pokémon.',
    exampleTexts: ['Heal 150 damage from 1 of your Psychic Pokémon.'],
    scope: 'trainer',
    importFrom: SUPPORT,
    importNames: [],
    params: [
      { key: 'amount', label: 'Heal', type: 'number', defaultValue: 150 },
      { key: 'type', label: 'Type', type: 'string' },
    ],
    patterns: [/^heal (\d+) damage from 1 of your (\w+) pok[eé]mon\.?$/i],
    paramCaptures: { 1: 'amount', 2: 'type' },
    generateCall: (params, ctx) => {
      const amount = num(params, 'amount', '150');
      const typeName = (params.type || 'psychic').toLowerCase();
      const enumId = typeEnumId(typeName);
      const fn = effectFnName(ctx.powerName || ctx.attackName || 'heal');
      const cond = `${fn}_condition`;
      const label = titleCase(typeName);
      return {
        lines: [fn],
        effectExpr: fn,
        condition: cond,
        helpers: [
          `def _is_${typeName}_pokemon(pokemon):\n    types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []\n    return PokemonTypes.${enumId}.value in types\n`,
          `def ${cond}(board, player_id):\n    return any(\n        _is_${typeName}_pokemon(p)\n        and p.get_attribute(AttrID.HP, 0) < effective_max_hp(board, p)\n        for p in board.pokemon_in_play(player_id)\n    )\n`,
          `async def ${fn}(ctx):\n    eligible = [\n        p for p in ctx.my_pokemon_in_play()\n        if _is_${typeName}_pokemon(p)\n        and p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)\n    ]\n    if not eligible:\n        return\n    target = await ctx.choose_pokemon(eligible, ${JSON.stringify(`Choose a ${label} Pokémon to heal`)})\n    if target is not None:\n        await ctx.heal(${amount}, target)\n`,
        ],
        imports: [
          { module: ATTR, names: ['AttrID', 'PokemonTypes'] },
          { module: 'spirit.game.session.passives', names: ['effective_max_hp'] },
        ],
      };
    },
  },

  // ── Search ──────────────────────────────────────────────────────────────
  {
    id: 'SEARCH_BASIC_TO_BENCH',
    name: 'search_to_bench',
    description: 'Search for a Basic Pokémon and bench it.',
    exampleTexts: [
      'Search your deck for a Basic Pokémon and put it onto your Bench. Then, shuffle your deck.',
    ],
    scope: 'both',
    importFrom: SUPPORT,
    importNames: ['search_to_bench'],
    params: [{ key: 'count', label: 'Count', type: 'number', defaultValue: 1 }],
    patterns: [
      /^search your deck for (?:a|1) basic pok[eé]mon and put it onto your bench\.?\s*then,?\s*shuffle your deck\.?$/i,
      /^search your deck for up to (\d+) basic pok[eé]mon and put them onto your bench\.?\s*then,?\s*shuffle your deck\.?$/i,
    ],
    paramCaptures: { 1: 'count' },
    generateCall: (params) => {
      const count = params.count && params.count !== '' ? num(params, 'count', '1') : '1';
      return effect(`search_to_bench(count=${count})`, imp(SUPPORT, 'search_to_bench'));
    },
  },
  {
    id: 'SEARCH_TO_HAND',
    name: 'search_to_hand',
    description: 'Search deck for up to N cards into hand.',
    exampleTexts: [
      'Search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck.',
    ],
    scope: 'both',
    importFrom: SUPPORT,
    importNames: ['search_to_hand'],
    params: [{ key: 'count', label: 'Count', type: 'number', defaultValue: 1 }],
    patterns: [
      /^search your deck for (?:a|1) card and put it into your hand\.?\s*then,?\s*shuffle your deck\.?$/i,
      /^search your deck for up to (\d+) cards? and put them into your hand\.?\s*then,?\s*shuffle your deck\.?$/i,
    ],
    paramCaptures: { 1: 'count' },
    generateCall: (params) => {
      const count = params.count && params.count !== '' ? num(params, 'count', '1') : '1';
      return effect(`search_to_hand(count=${count})`, imp(SUPPORT, 'search_to_hand'));
    },
  },
  {
    id: 'SEARCH_SUPPORTER_TO_HAND',
    name: 'luminous_sign',
    description: 'Search the deck for a Supporter card into hand.',
    exampleTexts: [
      'Search your deck for a Supporter card, reveal it, and put it into your hand. Then, shuffle your deck.',
    ],
    scope: 'both',
    importFrom: POKEMON,
    importNames: ['luminous_sign'],
    params: [],
    patterns: [
      /^search your deck for (?:a|1) supporter card,?\s*reveal it,?\s*and put it into your hand\.?\s*then,?\s*shuffle your deck\.?$/i,
    ],
    generateCall: () => effect('luminous_sign', imp(POKEMON, 'luminous_sign')),
  },
  {
    id: 'SEARCH_NO_RULE_BOX',
    name: 'search Pokémon without a Rule Box',
    description: 'Search the deck for a Pokémon that does not have a Rule Box.',
    exampleTexts: [
      "Search your deck for a Pokémon that doesn't have a Rule Box, reveal it, and put it into your hand. Then, shuffle your deck.",
    ],
    scope: 'trainer',
    importFrom: SUPPORT,
    importNames: ['search_to_hand'],
    params: [],
    patterns: [
      /^search your deck for (?:a|1) pok[eé]mon that doesn'?t have a rule box,?\s*reveal it,?\s*and put it into your hand\.?\s*then,?\s*shuffle your deck\.?$/i,
    ],
    generateCall: () => ({
      lines: ['_no_rule_box_pokemon'],
      effectExpr:
        'search_to_hand(\n        _no_rule_box_pokemon, count=1, minimum=0, reveal=True,\n        prompt="Choose a Pokémon that doesn\'t have a Rule Box.",\n    )',
      helpers: [
        'def _no_rule_box_pokemon(card):\n    return is_pokemon_card(card) and not has_rule_box(\n        getattr(card, "archetype_id", None) or ""\n    )\n',
      ],
      imports: [
        ...imp(SUPPORT, 'search_to_hand'),
        ...imp('spirit.game.session.effects', 'is_pokemon_card'),
        { module: DATA, names: ['has_rule_box'] },
      ],
    }),
  },
  {
    id: 'SEARCH_BASIC_STAGE1_STAGE2',
    name: 'search Basic, Stage 1, and Stage 2',
    description: 'Search the deck for one Basic, one Stage 1, and one Stage 2 Pokémon.',
    exampleTexts: [
      'Search your deck for a Basic Pokémon, a Stage 1 Pokémon, and a Stage 2 Pokémon, reveal them, and put them into your hand. Then, shuffle your deck.',
    ],
    scope: 'trainer',
    importFrom: SUPPORT,
    importNames: [],
    params: [],
    patterns: [
      /^search your deck for a basic pok[eé]mon, a stage 1 pok[eé]mon, and a stage 2 pok[eé]mon,?\s*reveal them,?\s*and put them into your hand\.?\s*then,?\s*shuffle your deck\.?$/i,
    ],
    generateCall: (params, ctx) => {
      const fn = effectFnName(ctx.powerName || ctx.attackName || 'dawn');
      return {
        lines: [fn],
        effectExpr: fn,
        helpers: [
          `async def ${fn}(ctx):\n    picks = []\n    for predicate, prompt in (\n        (is_basic_pokemon, "Choose a Basic Pokémon to put into your hand."),\n        (is_stage1_pokemon, "Choose a Stage 1 Pokémon to put into your hand."),\n        (is_stage2_pokemon, "Choose a Stage 2 Pokémon to put into your hand."),\n    ):\n        picks.extend(await ctx.search_deck(\n            predicate, count=1, minimum=0, prompt=prompt,\n        ))\n    await ctx.put_in_hand(picks, reveal=True)\n    await ctx.shuffle_deck()\n`,
        ],
        imports: [
          ...imp('spirit.game.session.effects', 'is_basic_pokemon', 'is_stage1_pokemon', 'is_stage2_pokemon'),
        ],
      };
    },
  },

  // ── Switch / gust ───────────────────────────────────────────────────────
  {
    id: 'SWITCH_SELF',
    name: 'switch_self_attack',
    description: 'Switch this Pokémon with a Benched Pokémon.',
    exampleTexts: ['Switch this Pokémon with 1 of your Benched Pokémon.'],
    scope: 'attack',
    importFrom: SUPPORT,
    importNames: ['switch_self_attack'],
    params: [],
    patterns: [
      /^switch this pok[eé]mon with 1 of your benched pok[eé]mon\.?$/i,
    ],
    generateCall: () =>
      effect('switch_self_attack()', imp(SUPPORT, 'switch_self_attack')),
  },
  {
    id: 'GUST',
    name: 'gust_attack',
    description: "Switch in 1 of opponent's Benched Pokémon.",
    exampleTexts: [
      "Switch in 1 of your opponent's Benched Pokémon to the Active Spot.",
    ],
    scope: 'attack',
    importFrom: SUPPORT,
    importNames: ['gust_attack'],
    params: [],
    patterns: [
      /^switch (?:in )?1 of your opponent'?s benched pok[eé]mon(?: to the active spot)?\.?$/i,
      /^you may switch (?:in )?1 of your opponent'?s benched pok[eé]mon(?: to the active spot)?\.?$/i,
    ],
    generateCall: () => effect('gust_attack()', imp(SUPPORT, 'gust_attack')),
  },
  {
    id: 'GUST_ABILITY',
    name: 'gust (Ability)',
    description: "Ability: switch in 1 of opponent's Benched Pokémon.",
    exampleTexts: [
      "Switch in 1 of your opponent's Benched Pokémon to the Active Spot.",
    ],
    scope: 'power',
    importFrom: '',
    importNames: [],
    params: [],
    patterns: [
      /^switch (?:in )?1 of your opponent'?s benched pok[eé]mon(?: to the active spot)?\.?$/i,
      /^you may switch (?:in )?1 of your opponent'?s benched pok[eé]mon(?: to the active spot)?\.?$/i,
    ],
    generateCall: (params, ctx) => {
      const fn = effectFnName(ctx.powerName || 'gust');
      const mayBlock =
        params.may === 'true'
          ? `    if not await ctx.ask_yes_no(\n            "Switch in 1 of your opponent's Benched Pokémon to the Active Spot?"):\n        return\n`
          : '';
      return {
        lines: [fn],
        effectExpr: fn,
        helpers: [
          `async def ${fn}(ctx):\n    bench = ctx.opponent_bench()\n    if not bench:\n        return\n${mayBlock}    target = await ctx.choose_pokemon(\n        bench, "Choose the opponent's new Active Pokémon"\n    )\n    if target is not None:\n        await ctx.switch_active(ctx.opponent_id, target)\n`,
        ],
        imports: [],
      };
    },
  },

  // ── Damage ignore effects ───────────────────────────────────────────────
  {
    id: 'DAMAGE_NOT_AFFECTED_BY_WR_AND_EFFECTS',
    name: 'ignore_effects_attack(W/R)',
    description: "Damage isn't affected by Weakness, Resistance, or effects on Active.",
    exampleTexts: [
      "This attack's damage isn't affected by Weakness or Resistance, or by any effects on your opponent's Active Pokémon.",
    ],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['ignore_effects_attack'],
    params: [],
    patterns: [
      /^this attack'?s damage isn'?t affected by weakness or resistance,? or by any effects on your opponent'?s active pok[eé]mon\.?$/i,
    ],
    generateCall: () =>
      effect(
        'ignore_effects_attack(ignore_weakness=True, ignore_resistance=True)',
        imp(ATTACKS, 'ignore_effects_attack'),
      ),
  },
  {
    id: 'DAMAGE_NOT_AFFECTED_BY_EFFECTS',
    name: 'ignore_effects_attack',
    description: "Damage isn't affected by effects on the opponent's Active Pokémon.",
    exampleTexts: [
      "This attack's damage isn't affected by any effects on your opponent's Active Pokémon.",
    ],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['ignore_effects_attack'],
    params: [],
    patterns: [
      /^this attack'?s damage isn'?t affected by any effects on your opponent'?s active pok[eé]mon\.?$/i,
    ],
    generateCall: () =>
      effect('ignore_effects_attack()', imp(ATTACKS, 'ignore_effects_attack')),
  },
  {
    id: 'LOCKS_NEXT_TURN',
    name: 'locks_next_turn',
    description: "During your next turn, this Pokémon can't use this attack.",
    exampleTexts: [
      "During your next turn, this Pokémon can't attack.",
      "During your next turn, this Pokémon can't use Mega Brave.",
    ],
    scope: 'attack',
    importFrom: '',
    importNames: [],
    params: [],
    patterns: [
      /^during your next turn, this pok[eé]mon can'?t (?:attack|use .+?)\.?$/i,
    ],
    generateCall: () => ({
      lines: ['locks_next_turn=True'],
      locksNextTurn: true,
      imports: [],
    }),
  },
  {
    id: 'TAKES_LESS_DAMAGE',
    name: 'takes_less_passive',
    description: 'This Pokémon takes X less damage from attacks.',
    exampleTexts: [
      'This Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).',
    ],
    scope: 'power',
    importFrom: PASSIVES,
    importNames: ['takes_less_passive'],
    params: [{ key: 'amount', label: 'Less damage', type: 'number', defaultValue: 30 }],
    patterns: [
      /^this pok[eé]mon takes (\d+) less damage from attacks(?: \(after applying weakness and resistance\))?\.?$/i,
    ],
    paramCaptures: { 1: 'amount' },
    generateCall: (params) => ({
      lines: [`passive=takes_less_passive(${num(params, 'amount', '30')})`],
      passive: `takes_less_passive(${num(params, 'amount', '30')})`,
      imports: imp(PASSIVES, 'takes_less_passive'),
    }),
  },
  {
    id: 'BONUS_IF_ACTIVE_EX',
    name: 'bonus_if(active is ex)',
    description: "If the opponent's Active is a Pokémon ex, this attack does X more damage.",
    exampleTexts: [
      "If your opponent's Active Pokémon is a Pokémon ex, this attack does 90 more damage.",
    ],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['bonus_if', 'active_is'],
    params: [{ key: 'bonus', label: 'Bonus', type: 'number', defaultValue: 90 }],
    patterns: [
      /^if your opponent'?s active pok[eé]mon is a pok[eé]mon ex,?\s*this attack does (\d+) more damage\.?$/i,
    ],
    paramCaptures: { 1: 'bonus' },
    generateCall: (params) =>
      effect(
        `bonus_if(active_is(lambda p: is_pokemon_ex(p.archetype_id)), ${num(params, 'bonus', '90')})`,
        [...imp(ATTACKS, 'bonus_if', 'active_is'), ...imp(DATA, 'is_pokemon_ex')],
      ),
  },
  {
    id: 'BONUS_IF_ENTERED_ACTIVE',
    name: 'bonus_if(entered Active this turn)',
    description: 'If this Pokémon moved Bench → Active this turn, do X more damage.',
    exampleTexts: [
      'If this Pokémon moved from your Bench to the Active Spot this turn, this attack does 170 more damage.',
    ],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['bonus_if'],
    params: [{ key: 'bonus', label: 'Bonus', type: 'number', defaultValue: 170 }],
    patterns: [
      /^if this pok[eé]mon moved from your bench to the active spot this turn,?\s*this attack does (\d+) more damage\.?$/i,
    ],
    paramCaptures: { 1: 'bonus' },
    generateCall: (params) => ({
      lines: ['_entered_active_this_turn'],
      effectExpr: `bonus_if(_entered_active_this_turn, ${num(params, 'bonus', '170')})`,
      helpers: [
        'def _entered_active_this_turn(ctx):\n    return ctx.entered_active_this_turn(ctx.attacker)\n',
      ],
      imports: imp(ATTACKS, 'bonus_if'),
    }),
  },
  {
    id: 'DAMAGE_PER_HAND',
    name: 'damage_per(count_hand)',
    description: 'This attack does X damage for each card in a hand.',
    exampleTexts: [
      "This attack does 50 damage for each card in your opponent's hand.",
      'This attack does 20 damage for each card in your hand.',
    ],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['damage_per', 'count_hand'],
    params: [
      { key: 'per', label: 'Damage per card', type: 'number', defaultValue: 50 },
      { key: 'side', label: 'Hand', type: 'string', defaultValue: 'opponent' },
    ],
    patterns: [
      /^this attack does (\d+) damage for each card in your (opponent'?s) hand\.?$/i,
      /^this attack does (\d+) damage for each card in (your) hand\.?$/i,
    ],
    paramCaptures: { 1: 'per', 2: 'side' },
    generateCall: (params) => {
      const side = /opponent/i.test(params.side || 'opponent') ? 'opponent' : 'mine';
      return effect(
        `damage_per(count_hand("${side}"), ${num(params, 'per', '50')})`,
        imp(ATTACKS, 'damage_per', 'count_hand'),
      );
    },
  },
  {
    id: 'PLACE_COUNTERS_PER_HAND',
    name: 'place_counters(count_hand)',
    description: "Place X damage counters on the opponent's Active for each card in your hand.",
    exampleTexts: [
      "Place 2 damage counters on your opponent's Active Pokémon for each card in your hand.",
    ],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['place_counters', 'count_hand'],
    params: [{ key: 'per', label: 'Counters per card', type: 'number', defaultValue: 2 }],
    patterns: [
      /^(?:place|put) (\d+) damage counters on your opponent'?s active pok[eé]mon for each card in your hand\.?$/i,
    ],
    paramCaptures: { 1: 'per' },
    generateCall: (params) =>
      effect(
        `place_counters(lambda ctx: ${num(params, 'per', '2')} * count_hand()(ctx))`,
        imp(ATTACKS, 'place_counters', 'count_hand'),
      ),
  },
  {
    id: 'REQUIRE_BENCHED_ALLY_IGNORE_WR',
    name: 'require benched ally, ignore W/R',
    description: "Does nothing without a named Benched ally; damage ignores Weakness and Resistance.",
    exampleTexts: [
      "If you don't have Lunatone on your Bench, this attack does nothing. This attack's damage isn't affected by Weakness or Resistance.",
    ],
    scope: 'attack',
    importFrom: ATTR,
    importNames: ['AttrID'],
    params: [{ key: 'ally', label: 'Ally name', type: 'string' }],
    patterns: [
      /^if you don'?t have (\w+) on your bench,?\s*this attack does nothing\.?\s*this attack'?s damage isn'?t affected by weakness or resistance\.?$/i,
    ],
    paramCaptures: { 1: 'ally' },
    generateCall: (params, ctx) => {
      const ally = params.ally || 'Ally';
      const fn = effectFnName(ctx.attackName || 'attack');
      return {
        lines: [fn],
        effectExpr: fn,
        helpers: [
          `async def ${fn}(ctx):\n    if not any(p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == ${JSON.stringify(ally)}\n               for p in ctx.my_bench()):\n        return\n    await ctx.deal_damage(ignore_weakness=True, ignore_resistance=True)\n`,
        ],
        imports: imp(ATTR, 'AttrID'),
      };
    },
  },
  {
    id: 'DISCARD_UP_TO_FOR_EACH_DAMAGE',
    name: 'discard up to N energy, X damage each',
    description: 'Discard up to N Energy from this Pokémon; deal X damage per discarded card.',
    exampleTexts: [
      'Discard up to 2 Energy cards from this Pokémon, and this attack does 120 damage for each card you discarded in this way.',
    ],
    scope: 'attack',
    importFrom: '',
    importNames: [],
    params: [
      { key: 'count', label: 'Up to', type: 'number', defaultValue: 2 },
      { key: 'per', label: 'Damage each', type: 'number', defaultValue: 120 },
    ],
    patterns: [
      /^discard up to (\d+) energy(?: cards)? from this pok[eé]mon,?\s*and this attack does (\d+) damage for each card you discarded in this way\.?$/i,
    ],
    paramCaptures: { 1: 'count', 2: 'per' },
    generateCall: (params, ctx) => {
      const count = num(params, 'count', '2');
      const per = num(params, 'per', '120');
      const fn = effectFnName(ctx.attackName || 'attack');
      return {
        lines: [fn],
        effectExpr: fn,
        helpers: [
          `async def ${fn}(ctx):\n    discarded = []\n    if ctx.attached_energies(ctx.attacker) and await ctx.ask_yes_no(\n            ${JSON.stringify(`Discard up to ${count} Energy from this Pokémon?`)}):\n        discarded = await ctx.discard_energy_from(\n            ctx.attacker, ${count}, minimum=0,\n            prompt=${JSON.stringify(`Choose up to ${count} Energy to discard`)})\n    amount = ${per} * len(discarded)\n    if amount > 0:\n        await ctx.deal_damage(amount)\n`,
        ],
        imports: [],
      };
    },
  },
  {
    id: 'ATTACH_FROM_DISCARD_TO_BENCH',
    name: 'attach from discard to bench',
    description: 'Attach up to N Basic (typed) Energy from discard to the Bench.',
    exampleTexts: [
      'Attach up to 3 Basic Fighting Energy cards from your discard pile to your Benched Pokémon in any way you like.',
    ],
    scope: 'attack',
    importFrom: SUPPORT,
    importNames: ['distribute_energy'],
    params: [
      { key: 'count', label: 'Up to', type: 'number', defaultValue: 3 },
      { key: 'type', label: 'Energy type', type: 'string' },
    ],
    patterns: [
      /^attach up to (\d+) basic(?: (\w+))? energy cards? from your discard pile to your benched pok[eé]mon in any way you like\.?$/i,
    ],
    paramCaptures: { 1: 'count', 2: 'type' },
    generateCall: (params, ctx) => {
      const count = num(params, 'count', '3');
      const typeName = (params.type || '').toLowerCase();
      const enumId = typeName ? typeEnumId(typeName) : '';
      const label = typeName ? `Basic ${titleCase(typeName)} Energy` : 'Basic Energy';
      const fn = effectFnName(ctx.attackName || 'attach_energy');
      const pred = typeName ? `_is_basic_${typeName}_energy` : 'is_basic_energy_card';
      const predHelper = typeName
        ? `def ${pred}(card):\n    return is_basic_energy_card(card) and energy_provides_type(\n        card, PokemonTypes.${enumId}.value)\n`
        : '';
      const imports: PrefabImport[] = [
        ...imp(SUPPORT, 'distribute_energy'),
        ...imp(TRAINERS, 'is_basic_energy_card'),
      ];
      if (typeName) {
        imports.push(...imp(POKEMON, 'energy_provides_type'));
        imports.push({ module: ATTR, names: ['PokemonTypes'] });
      }
      return {
        lines: [fn],
        effectExpr: fn,
        helpers: [
          predHelper,
          `async def ${fn}(ctx):\n    await ctx.deal_damage()\n    bench = ctx.my_bench()\n    if not bench:\n        return\n    energies = [c for c in ctx.discard_pile() if ${pred}(c)]\n    if not energies:\n        return\n    picks = await ctx.choose_cards(\n        energies, ${count}, minimum=0,\n        prompt=${JSON.stringify(`Choose up to ${count} ${label} cards to attach to your Benched Pokémon`)},\n    )\n    if picks:\n        await distribute_energy(ctx, picks, bench)\n`,
        ].filter(Boolean),
        imports,
      };
    },
  },
  {
    id: 'DISCARD_TYPED_ENERGY_DRAW_IF_NAMED',
    name: 'discard typed energy, draw, if named Pokémon in play',
    description: 'If a named Pokémon is in play, discard a Basic typed Energy from hand and draw.',
    exampleTexts: [
      'If you have Solrock in play, you may discard a Basic Fighting Energy card from your hand in order to use this Ability. Draw 3 cards.',
    ],
    scope: 'power',
    importFrom: TRAINERS,
    importNames: ['is_basic_energy_card'],
    params: [
      { key: 'ally', label: 'Ally name', type: 'string' },
      { key: 'type', label: 'Energy type', type: 'string' },
      { key: 'count', label: 'Draw', type: 'number', defaultValue: 3 },
    ],
    patterns: [
      /^if you have (\w+) in play,?\s*you may discard (?:a|1) basic (\w+) energy(?: card)? from your hand in order to use this ability\.?\s*draw (\d+) cards?\.?$/i,
    ],
    paramCaptures: { 1: 'ally', 2: 'type', 3: 'count' },
    generateCall: (params, ctx) => {
      const ally = params.ally || 'Ally';
      const typeName = (params.type || 'fighting').toLowerCase();
      const enumId = typeEnumId(typeName);
      const draw = num(params, 'count', '3');
      const fn = effectFnName(ctx.powerName || 'ability');
      const pred = `_is_basic_${typeName}_energy`;
      const cond = `${fn}_condition`;
      return {
        lines: [fn],
        effectExpr: fn,
        condition: cond,
        helpers: [
          `def ${pred}(card):\n    types = card.get_attribute(AttrID.POKEMON_TYPES) or []\n    return is_basic_energy_card(card) and PokemonTypes.${enumId}.value in types\n`,
          `def ${cond}(board, player_id, pokemon):\n    if not any(p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == ${JSON.stringify(ally)}\n               for p in board.pokemon_in_play(player_id)):\n        return False\n    hand = board.find_player_area(player_id, "hand")\n    return bool(hand) and any(${pred}(c) for c in hand.children)\n`,
          `async def ${fn}(ctx):\n    discarded = await ctx.discard_from_hand(\n        1, predicate=${pred},\n        prompt=${JSON.stringify(`Discard a Basic ${titleCase(typeName)} Energy card`)},\n    )\n    if discarded:\n        await ctx.draw_cards(${draw})\n`,
        ],
        imports: [
          ...imp(TRAINERS, 'is_basic_energy_card'),
          { module: ATTR, names: ['AttrID', 'PokemonTypes'] },
        ],
      };
    },
  },

  // ── Trainer draw helpers (Judge-like) ───────────────────────────────────
  {
    id: 'SHUFFLE_HAND_DRAW',
    name: 'shuffle_hand_into_deck_draw',
    description: 'Each player shuffles hand into deck and draws N.',
    exampleTexts: [
      'Each player shuffles their hand into their deck and draws 4 cards.',
    ],
    scope: 'trainer',
    importFrom: SUPPORT,
    importNames: ['shuffle_hand_into_deck_draw'],
    params: [{ key: 'count', label: 'Draw', type: 'number', defaultValue: 4 }],
    patterns: [
      /^each player shuffles (?:their|his or her) hand into (?:their|his or her) deck and draws (\d+) cards?\.?$/i,
    ],
    paramCaptures: { 1: 'count' },
    generateCall: (params) =>
      effect(
        `shuffle_hand_into_deck_draw(${num(params, 'count', '4')})`,
        imp(SUPPORT, 'shuffle_hand_into_deck_draw'),
      ),
  },
  {
    id: 'SHUFFLE_YOUR_HAND_DRAW_PRIZES',
    name: 'shuffle hand, draw, prize bonus',
    description: 'Shuffle your hand into your deck, draw N, or M if exactly P prizes remain.',
    exampleTexts: [
      'Shuffle your hand into your deck. Then, draw 6 cards. If you have exactly 6 Prize cards remaining, draw 8 cards instead.',
    ],
    scope: 'trainer',
    importFrom: ATTACKS,
    importNames: ['count_prizes_remaining'],
    params: [
      { key: 'base', label: 'Draw', type: 'number', defaultValue: 6 },
      { key: 'prizes', label: 'Prize count', type: 'number', defaultValue: 6 },
      { key: 'bonus', label: 'Bonus draw', type: 'number', defaultValue: 8 },
    ],
    patterns: [
      /^shuffle your hand into your deck\.?\s*then,?\s*draw (\d+) cards?\.?\s*if you have exactly (\d+) prize cards remaining,?\s*draw (\d+) cards instead\.?$/i,
    ],
    paramCaptures: { 1: 'base', 2: 'prizes', 3: 'bonus' },
    generateCall: (params, ctx) => {
      const base = num(params, 'base', '6');
      const prizes = num(params, 'prizes', '6');
      const bonus = num(params, 'bonus', '8');
      const fn = effectFnName(ctx.attackName || ctx.powerName || 'shuffle_draw');
      return {
        lines: [fn],
        effectExpr: fn,
        helpers: [
          `async def ${fn}(ctx):\n    n = ${bonus} if count_prizes_remaining("mine")(ctx) == ${prizes} else ${base}\n    await ctx.shuffle_into_deck(ctx.hand(), ctx.player_id)\n    await ctx.draw_cards(n)\n`,
        ],
        imports: imp(ATTACKS, 'count_prizes_remaining'),
      };
    },
  },
  {
    id: 'SHUFFLE_YOUR_HAND_DRAW',
    name: 'shuffle your hand, then draw',
    description: 'Shuffle your hand into your deck, then draw N.',
    exampleTexts: ['Shuffle your hand into your deck. Then, draw 6 cards.'],
    scope: 'trainer',
    importFrom: '',
    importNames: [],
    params: [{ key: 'count', label: 'Draw', type: 'number', defaultValue: 6 }],
    patterns: [
      /^shuffle your hand into your deck\.?\s*then,?\s*draw (\d+) cards?\.?$/i,
    ],
    paramCaptures: { 1: 'count' },
    generateCall: (params, ctx) => {
      const count = num(params, 'count', '6');
      const fn = effectFnName(ctx.attackName || ctx.powerName || 'shuffle_draw');
      return {
        lines: [fn],
        effectExpr: fn,
        helpers: [
          `async def ${fn}(ctx):\n    await ctx.shuffle_into_deck(ctx.hand(), ctx.player_id)\n    await ctx.draw_cards(${count})\n`,
        ],
        imports: [],
      };
    },
  },
  {
    id: 'TURN_DAMAGE_BOOST',
    name: 'TurnDamageModifier',
    description: "This turn, your Pokémon's attacks do X more damage to the opponent's Active.",
    exampleTexts: [
      "During this turn, attacks used by your Pokémon do 30 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
      "During this turn, your Pokémon's attacks do 30 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
    ],
    scope: 'trainer',
    importFrom: 'spirit.game.session.passives',
    importNames: ['TurnDamageModifier'],
    params: [{ key: 'amount', label: 'Bonus', type: 'number', defaultValue: 30 }],
    patterns: [
      /^during this turn, (?:attacks used by your pok[eé]mon|your pok[eé]mon'?s attacks) do (\d+) more damage to your opponent'?s active pok[eé]mon(?: \(before applying weakness and resistance\))?\.?$/i,
    ],
    paramCaptures: { 1: 'amount' },
    generateCall: (params, ctx) => {
      const amount = num(params, 'amount', '30');
      const fn = effectFnName(ctx.attackName || ctx.powerName || 'turn_damage');
      return {
        lines: [fn],
        effectExpr: fn,
        helpers: [
          `async def ${fn}(ctx):\n    ctx.add_turn_damage_modifier(TurnDamageModifier(${amount}, ctx.player_id))\n    for pokemon in ctx.my_pokemon_in_play():\n        await ctx.add_stat_visualization(\n            pokemon, "Positive", "DamageDealtIncreased", card_text="+${amount} damage"\n        )\n`,
        ],
        imports: [{ module: 'spirit.game.session.passives', names: ['TurnDamageModifier'] }],
      };
    },
  },
  {
    id: 'SEARCH_TYPE_ENERGY_OR_BASIC',
    name: 'search typed Energy or Basic Pokémon',
    description: 'Search for a Basic typed Energy or a Basic Pokémon of that type.',
    exampleTexts: [
      'Search your deck for a Basic Fighting Energy or a Basic Fighting Pokémon, reveal it, and put it into your hand. Then, shuffle your deck.',
      'Search your deck for a Psychic Energy card or a Basic Psychic Pokémon, reveal it, and put it into your hand. Then, shuffle your deck.',
    ],
    scope: 'trainer',
    importFrom: SUPPORT,
    importNames: ['search_to_hand'],
    params: [{ key: 'type', label: 'Type', type: 'string' }],
    patterns: [
      /^search your deck for (?:a|1) basic (\w+) energy(?: card)? or (?:a|1) basic \1 pok[eé]mon,?\s*reveal it,?\s*and put it into your hand\.?\s*then,?\s*shuffle (?:the|your) deck\.?$/i,
      /^search your deck for (?:a|1) (\w+) energy(?: card)? or (?:a|1) basic \1 pok[eé]mon,?\s*reveal it,?\s*and put it into your hand\.?\s*then,?\s*shuffle (?:the|your) deck\.?$/i,
    ],
    paramCaptures: { 1: 'type' },
    generateCall: (params) => {
      const typeName = (params.type || 'fighting').toLowerCase();
      const enumId = typeEnumId(typeName);
      const fn = `_${typeName}_energy_or_basic`;
      const label = titleCase(typeName);
      return {
        lines: [fn],
        effectExpr: `search_to_hand(\n        ${fn}, count=1, minimum=0, reveal=True,\n        prompt="Choose a Basic ${label} Energy or a Basic ${label} Pokémon.",\n    )`,
        helpers: [
          `def ${fn}(card):\n    types = card.get_attribute(AttrID.POKEMON_TYPES) or []\n    if PokemonTypes.${enumId}.value not in types:\n        return False\n    return is_basic_energy_card(card) or is_basic_pokemon(card)\n`,
        ],
        imports: [
          ...imp(SUPPORT, 'search_to_hand'),
          ...imp('spirit.game.session.effects', 'is_basic_pokemon'),
          ...imp(TRAINERS, 'is_basic_energy_card'),
          { module: ATTR, names: ['AttrID', 'PokemonTypes'] },
        ],
      };
    },
  },
  {
    id: 'STADIUM_BENCH_COUNTERS',
    name: 'stadium: counters on benched Basics',
    description: 'Whenever a Basic (optionally non-type) is benched, place damage counters on it.',
    exampleTexts: [
      'Whenever any player puts a Basic non-Darkness Pokémon onto their Bench during their turn, place 2 damage counters on that Pokémon.',
      'Whenever either player puts a Basic Pokémon from their hand onto their Bench, put 2 damage counters on that Pokémon.',
    ],
    scope: 'trainer',
    importFrom: DATA,
    importNames: ['Ability', 'Triggers'],
    params: [
      { key: 'excludeType', label: 'Exclude type', type: 'string' },
      { key: 'counters', label: 'Counters', type: 'number', defaultValue: 2 },
    ],
    patterns: [
      /^whenever (?:any|either) player puts a basic(?: non-(\w+))? pok[eé]mon(?: from their hand)? onto (?:their|his or her) bench(?: during their turn)?,?\s*(?:put|place) (\d+) damage counters on that pok[eé]mon\.?$/i,
    ],
    paramCaptures: { 1: 'excludeType', 2: 'counters' },
    generateCall: (params, ctx) => {
      const excludeRaw = (params.excludeType || '').trim();
      const counters = num(params, 'counters', '2');
      const damage = String(Number(counters) * 10);
      const fn = `${effectFnName(ctx.attackName || ctx.powerName || 'stadium')}_watch`;
      const excludeId = excludeRaw ? typeEnumId(excludeRaw) : '';
      const excludeBlock = excludeId
        ? `    types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []\n    if PokemonTypes.${excludeId}.value in types:\n        return\n`
        : '';
      const imports: PrefabImport[] = imp(DATA, 'Ability', 'Triggers');
      if (excludeId) imports.push({ module: ATTR, names: ['AttrID', 'PokemonTypes'] });
      return {
        lines: [fn],
        effectExpr: fn,
        trigger: 'Triggers.ON_POKEMON_BENCHED',
        helpers: [
          `async def ${fn}(ctx):\n    pokemon = ctx.benched_pokemon\n    if pokemon is None:\n        return\n${excludeBlock}    await ctx.deal_damage(${damage}, target=pokemon, apply_modifiers=False,\n                          as_counters=True)\n`,
        ],
        imports,
      };
    },
  },
  {
    id: 'PROFESSORS_RESEARCH',
    name: 'professors_research',
    description: 'Discard your hand and draw 7.',
    exampleTexts: ['Discard your hand and draw 7 cards.'],
    scope: 'trainer',
    importFrom: TRAINERS,
    importNames: ['professors_research'],
    params: [],
    patterns: [
      /^discard your hand and draw 7 cards?\.?$/i,
    ],
    generateCall: () =>
      effect('professors_research', imp(TRAINERS, 'professors_research')),
  },
  {
    id: 'TRAINER_SWITCH',
    name: 'switch',
    description: 'Switch your Active with a Benched Pokémon.',
    exampleTexts: ['Switch your Active Pokémon with 1 of your Benched Pokémon.'],
    scope: 'trainer',
    importFrom: TRAINERS,
    importNames: ['switch'],
    params: [],
    patterns: [
      /^switch your active pok[eé]mon with 1 of your benched pok[eé]mon\.?$/i,
    ],
    generateCall: () => effect('switch', imp(TRAINERS, 'switch')),
  },
  {
    id: 'BOSS_ORDERS',
    name: 'bosss_orders',
    description: "Switch in 1 of the opponent's Benched Pokémon.",
    exampleTexts: [
      "Switch 1 of your opponent's Benched Pokémon with your opponent's Active Pokémon.",
    ],
    scope: 'trainer',
    importFrom: TRAINERS,
    importNames: ['bosss_orders'],
    params: [],
    patterns: [
      /^switch 1 of your opponent'?s benched pok[eé]mon with (?:your opponent'?s|their) active pok[eé]mon\.?$/i,
      /^switch in 1 of your opponent'?s benched pok[eé]mon(?: to the active spot)?\.?$/i,
    ],
    generateCall: () => effect('bosss_orders', imp(TRAINERS, 'bosss_orders')),
  },
  {
    id: 'ULTRA_BALL',
    name: 'ultra_ball',
    description: 'Discard 2, search any Pokémon.',
    exampleTexts: [
      'You may discard 2 cards from your hand. If you do, search your deck for a Pokémon, reveal it, and put it into your hand. Then, shuffle your deck.',
    ],
    scope: 'trainer',
    importFrom: TRAINERS,
    importNames: ['ultra_ball', 'hand_size_at_least'],
    params: [],
    patterns: [
      /^you may discard 2 cards(?: from your hand)?\.?\s*if you do,?\s*search your deck for (?:a|1) pok[eé]mon,?\s*reveal it,?\s*and put it into your hand\.?\s*then,?\s*shuffle your deck\.?$/i,
    ],
    generateCall: () => ({
      ...effect('ultra_ball', imp(TRAINERS, 'ultra_ball', 'hand_size_at_least')),
      condition: 'hand_size_at_least(3)',
    }),
  },
  {
    id: 'QUICK_BALL',
    name: 'quick_ball',
    description: 'Discard 1, search a Basic Pokémon.',
    exampleTexts: [
      'You may discard 1 card from your hand. If you do, search your deck for a Basic Pokémon, reveal it, and put it into your hand. Then, shuffle your deck.',
    ],
    scope: 'trainer',
    importFrom: TRAINERS,
    importNames: ['quick_ball', 'hand_size_at_least'],
    params: [],
    patterns: [
      /^you may discard (?:1|a) card(?: from your hand)?\.?\s*if you do,?\s*search your deck for (?:a|1) basic pok[eé]mon,?\s*reveal it,?\s*and put it into your hand\.?\s*then,?\s*shuffle your deck\.?$/i,
    ],
    generateCall: () => ({
      ...effect('quick_ball', imp(TRAINERS, 'quick_ball', 'hand_size_at_least')),
      condition: 'hand_size_at_least(2)',
    }),
  },
  {
    id: 'SHUFFLE_ENERGY_THEN_SNIPE',
    name: 'shuffle Energy into deck, then snipe',
    description: 'Shuffle all Energy from this Pokémon into the deck, then deal X to 1 of the opponent\'s Pokémon.',
    exampleTexts: [
      "Shuffle all Energy attached to this Pokémon into your deck, and this attack does 220 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
    ],
    scope: 'attack',
    importFrom: ATTACKS,
    importNames: ['snipe_attack'],
    params: [{ key: 'amount', label: 'Damage', type: 'number', defaultValue: 220 }],
    patterns: [
      /^shuffle all energy attached to this pok[eé]mon into your deck,?\s*and this attack does (\d+) damage to 1 of your opponent'?s pok[eé]mon\.?(?:\s*\(don't apply weakness and resistance for benched pok[eé]mon\.\))?$/i,
    ],
    paramCaptures: { 1: 'amount' },
    generateCall: (params, ctx) => {
      const amount = num(params, 'amount', '220');
      const fn = effectFnName(ctx.attackName || 'sonic_ripper');
      return {
        lines: [fn],
        effectExpr: fn,
        helpers: [
          `async def ${fn}(ctx):\n    energies = list(ctx.attached_energies(ctx.attacker))\n    if energies:\n        await ctx.shuffle_into_deck(energies, player_id=ctx.player_id)\n    await snipe_attack(${amount}, pool="any")(ctx)\n`,
        ],
        imports: imp(ATTACKS, 'snipe_attack'),
      };
    },
  },
  {
    id: 'ATTACH_TYPED_ENERGY_FROM_DISCARD_TO_TYPED_BENCH',
    name: 'attach typed Energy from discard to typed Bench',
    description: 'Attach a Basic [Type] Energy from discard to 1 Benched [Type] Pokémon.',
    exampleTexts: [
      'Attach a Basic Psychic Energy card from your discard pile to 1 of your Benched Psychic Pokémon.',
    ],
    scope: 'trainer',
    importFrom: TRAINERS,
    importNames: ['is_basic_energy_card'],
    params: [{ key: 'type', label: 'Type', type: 'string' }],
    patterns: [
      /^attach (?:a|1) basic (\w+) energy(?: card)? from your discard pile to 1 of your benched \1 pok[eé]mon\.?$/i,
    ],
    paramCaptures: { 1: 'type' },
    generateCall: (params, ctx) => {
      const typeName = (params.type || 'psychic').toLowerCase();
      const enumId = typeEnumId(typeName);
      const fn = effectFnName(ctx.powerName || ctx.attackName || 'wondrous_patch');
      const cond = `${fn}_condition`;
      const label = titleCase(typeName);
      return {
        lines: [fn],
        effectExpr: fn,
        condition: cond,
        helpers: [
          `def _is_basic_${typeName}_energy(card):\n    return is_basic_energy_card(card) and energy_provides_type(\n        card, PokemonTypes.${enumId}.value)\n`,
          `def _is_${typeName}_pokemon(pokemon):\n    types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []\n    return PokemonTypes.${enumId}.value in types\n`,
          `def ${cond}(board, player_id):\n    discard = board.find_player_area(player_id, "discard")\n    has_energy = bool(discard) and any(_is_basic_${typeName}_energy(c) for c in discard.children)\n    bench = board.find_player_area(player_id, "bench")\n    has_bench = bool(bench) and any(_is_${typeName}_pokemon(p) for p in bench.children)\n    return has_energy and has_bench\n`,
          `async def ${fn}(ctx):\n    energy = [c for c in ctx.discard_pile() if _is_basic_${typeName}_energy(c)]\n    bench = [p for p in ctx.my_bench() if _is_${typeName}_pokemon(p)]\n    if not energy or not bench:\n        return\n    picks = await ctx.choose_cards(\n        energy, 1, minimum=1,\n        prompt=${JSON.stringify(`Choose a Basic ${label} Energy card to attach.`)},\n    )\n    if not picks:\n        return\n    target = await ctx.choose_pokemon(bench, ${JSON.stringify(`Choose 1 of your Benched ${label} Pokémon`)})\n    if target is None:\n        return\n    await ctx.attach_energy(picks[0], target)\n`,
        ],
        imports: [
          ...imp(TRAINERS, 'is_basic_energy_card'),
          ...imp(POKEMON, 'energy_provides_type'),
          { module: ATTR, names: ['AttrID', 'PokemonTypes'] },
        ],
      };
    },
  },
  {
    id: 'SEARCH_TYPED_ENERGY_ATTACH_BENCH_COUNTERS',
    name: 'search typed Energy, attach to typed Bench, counters',
    description: 'Search a Basic [Type] Energy, attach to a Benched [Type] Pokémon, place counters.',
    exampleTexts: [
      'Search your deck for a Basic Darkness Energy card and attach it to 1 of your Benched Darkness Pokémon. Then, shuffle your deck. If you attached Energy to a Pokémon in this way, place 2 damage counters on that Pokémon.',
    ],
    scope: 'power',
    importFrom: TRAINERS,
    importNames: ['is_basic_energy_card'],
    params: [
      { key: 'type', label: 'Type', type: 'string' },
      { key: 'counters', label: 'Counters', type: 'number', defaultValue: 2 },
    ],
    patterns: [
      /^search your deck for (?:a|1) basic (\w+) energy(?: card)? and attach it to 1 of your benched \1 pok[eé]mon\.?\s*then,?\s*shuffle your deck\.?\s*if you attached energy to a pok[eé]mon in this way,?\s*place (\d+) damage counters on that pok[eé]mon\.?$/i,
    ],
    paramCaptures: { 1: 'type', 2: 'counters' },
    generateCall: (params, ctx) => {
      const typeName = (params.type || 'darkness').toLowerCase();
      const enumId = typeEnumId(typeName);
      const counters = num(params, 'counters', '2');
      const damage = String(Number(counters) * 10);
      const fn = effectFnName(ctx.powerName || 'sinister_surge');
      const cond = `${fn}_condition`;
      const label = titleCase(typeName);
      return {
        lines: [fn],
        effectExpr: fn,
        condition: cond,
        helpers: [
          `def _is_basic_${typeName}_energy(card):\n    return is_basic_energy_card(card) and energy_provides_type(\n        card, PokemonTypes.${enumId}.value)\n`,
          `def _is_${typeName}_pokemon(pokemon):\n    types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []\n    return PokemonTypes.${enumId}.value in types\n`,
          `def ${cond}(board, player_id, pokemon=None):\n    bench = board.find_player_area(player_id, "bench")\n    return bool(bench) and any(_is_${typeName}_pokemon(p) for p in bench.children)\n`,
          `async def ${fn}(ctx):\n    if not await ctx.ask_yes_no(\n        ${JSON.stringify(`Search your deck for a Basic ${label} Energy card and attach it to 1 of your Benched ${label} Pokémon?`)}\n    ):\n        return\n    picks = await ctx.search_deck(\n        _is_basic_${typeName}_energy, count=1, minimum=0,\n        prompt=${JSON.stringify(`Choose a Basic ${label} Energy card to attach.`)},\n    )\n    if picks:\n        candidates = [p for p in ctx.my_bench() if _is_${typeName}_pokemon(p)]\n        if candidates:\n            target = await ctx.choose_pokemon(\n                candidates, ${JSON.stringify(`Choose a Benched ${label} Pokémon to attach the Energy to`)}\n            )\n            if target is not None:\n                await ctx.attach_energy(picks[0], target)\n                await ctx.deal_damage(\n                    ${damage}, target=target, apply_modifiers=False, as_counters=True\n                )\n    await ctx.shuffle_deck()\n`,
        ],
        imports: [
          ...imp(TRAINERS, 'is_basic_energy_card'),
          ...imp(POKEMON, 'energy_provides_type'),
          { module: ATTR, names: ['AttrID', 'PokemonTypes'] },
        ],
      };
    },
  },
  {
    id: 'PRIZE_GATE_ATTACH_TO_STAGE2',
    name: 'more Prizes, attach Energy to Stage 2',
    description: 'Playable with more Prizes remaining; attach up to N Basic Energy from discard to 1 Stage 2.',
    exampleTexts: [
      'You can use this card only if you have more Prize cards remaining than your opponent. Attach up to 2 Basic Energy cards from your discard pile to 1 of your Stage 2 Pokémon.',
    ],
    scope: 'trainer',
    importFrom: SUPPORT,
    importNames: ['more_prizes_remaining_than_opponent'],
    params: [{ key: 'count', label: 'Up to', type: 'number', defaultValue: 2 }],
    patterns: [
      /^you can use this card only if you have more prize cards remaining than your opponent\.?\s*attach up to (\d+) basic energy cards? from your discard pile to 1 of your stage 2 pok[eé]mon\.?$/i,
    ],
    paramCaptures: { 1: 'count' },
    generateCall: (params, ctx) => {
      const count = num(params, 'count', '2');
      const fn = effectFnName(ctx.powerName || ctx.attackName || 'rosas_encouragement');
      const cond = `${fn}_condition`;
      return {
        lines: [fn],
        effectExpr: fn,
        condition: cond,
        helpers: [
          `def ${cond}(board, player_id):\n    if not more_prizes_remaining_than_opponent(board, player_id):\n        return False\n    discard = board.find_player_area(player_id, "discard")\n    has_energy = bool(discard) and any(is_basic_energy_card(c) for c in discard.children)\n    has_stage2 = any(is_stage2_pokemon(p) for p in board.pokemon_in_play(player_id))\n    return has_energy and has_stage2\n`,
          `async def ${fn}(ctx):\n    energy = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]\n    targets = [p for p in ctx.my_pokemon_in_play() if is_stage2_pokemon(p)]\n    if not energy or not targets:\n        return\n    target = await ctx.choose_pokemon(targets, "Choose 1 of your Stage 2 Pokémon")\n    if target is None:\n        return\n    picks = await ctx.choose_cards(\n        energy, ${count}, minimum=0,\n        prompt=${JSON.stringify(`Choose up to ${count} Basic Energy cards to attach.`)},\n    )\n    for card in picks:\n        await ctx.attach_energy(card, target)\n`,
        ],
        imports: [
          ...imp(SUPPORT, 'more_prizes_remaining_than_opponent'),
          ...imp(TRAINERS, 'is_basic_energy_card'),
          ...imp('spirit.game.session.effects', 'is_stage2_pokemon'),
        ],
      };
    },
  },
  {
    id: 'STADIUM_TERA_ATTACKS_COST_MORE',
    name: 'stadium: Tera attacks cost C more',
    description: 'Attacks used by each Tera Pokémon in play cost Colorless more.',
    exampleTexts: [
      'Attacks used by each Tera Pokémon in play (both yours and your opponent\'s) cost Colorless more.',
    ],
    scope: 'trainer',
    importFrom: DATA,
    importNames: ['subtypes_for'],
    params: [],
    patterns: [
      /^attacks used by each tera pok[eé]mon in play(?: \(both yours and your opponent'?s\))? cost .+ more\.?$/i,
    ],
    generateCall: (_params, ctx) => {
      const cls = `${pascalIdent(ctx.powerName || 'Stadium')}Passive`;
      return {
        lines: [cls],
        passive: `${cls}()`,
        helpers: [
          `class ${cls}(Passive):\n    def modify_attack_cost(self, cost, pokemon, carrier, board):\n        if "Tera" in subtypes_for(pokemon.archetype_id):\n            cost["Colorless"] = cost.get("Colorless", 0) + 1\n        return cost\n`,
        ],
        imports: [
          { module: DATA, names: ['subtypes_for'] },
          { module: 'spirit.game.session.passives', names: ['Passive'] },
        ],
      };
    },
  },
  {
    id: 'STADIUM_BENCH_COUNTER_SHIELD',
    name: 'stadium: prevent counters on Bench',
    description: 'Prevent damage counters on Benched Pokémon from opposing Pokémon attacks and Abilities.',
    exampleTexts: [
      "Prevent all damage counters from being placed on Benched Pokémon (both yours and your opponent's) by effects of attacks and Abilities from the opponent's Pokémon. (Damage from attacks is still taken.)",
    ],
    scope: 'trainer',
    importFrom: '',
    importNames: [],
    params: [],
    patterns: [
      /^prevent all damage counters from being placed on benched pok[eé]mon(?: \(both yours and your opponent'?s\))? by effects of attacks and abilities from the opponent'?s pok[eé]mon\.?$/i,
    ],
    generateCall: (_params, ctx) => {
      const cls = `${pascalIdent(ctx.powerName || 'Stadium')}Passive`;
      return {
        lines: [cls],
        passive: `${cls}()`,
        helpers: [
          `class ${cls}(Passive):\n    def blocks_damage_counters(self, target, carrier):\n        parent = target.parent\n        return bool(parent) and parent.get_attribute(AttrID.NAME) == "bench"\n`,
        ],
        imports: [
          { module: ATTR, names: ['AttrID'] },
          { module: 'spirit.game.session.passives', names: ['Passive'] },
        ],
      };
    },
  },
  {
    id: 'ENERGY_ATTACK_EFFECT_SHIELD',
    name: 'energy: attack-effect shield',
    description: 'Prevent attack effects done to the (typed) Pokémon this Energy is attached to.',
    exampleTexts: [
      "Prevent all effects of attacks used by your opponent's Pokémon done to the Fighting Pokémon this card is attached to.",
      "Prevent all effects of attacks used by your opponent's Pokémon done to the Pokémon this card is attached to.",
    ],
    scope: 'energy',
    importFrom: PASSIVES,
    importNames: ['attack_effect_shield_passive'],
    params: [{ key: 'type', label: 'Type', type: 'string' }],
    patterns: [
      /^prevent all effects of attacks used by your opponent'?s pok[eé]mon done to the(?: (\w+))? pok[eé]mon this card is attached to\.?$/i,
    ],
    paramCaptures: { 1: 'type' },
    generateCall: (params) => {
      const typeName = (params.type || '').toLowerCase();
      const enumId = typeName ? typeEnumId(typeName) : '';
      const arg = enumId ? `pokemon_type=PokemonTypes.${enumId}` : '';
      const imports: PrefabImport[] = imp(PASSIVES, 'attack_effect_shield_passive');
      if (enumId) imports.push({ module: ATTR, names: ['PokemonTypes'] });
      return {
        lines: [`attack_effect_shield_passive(${arg})`],
        passive: `attack_effect_shield_passive(${arg})`,
        imports,
      };
    },
  },
  {
    id: 'ENERGY_ON_ATTACH_SEARCH_BASIC_TO_BENCH',
    name: 'energy: on attach, bench Basic Pokémon',
    description: 'When attached from hand to a typed Pokémon, search up to N Basic [Type] onto the Bench.',
    exampleTexts: [
      'When you attach this card from your hand to a Psychic Pokémon, search your deck for up to 2 Basic Psychic Pokémon and put them onto your Bench. Then, shuffle your deck.',
    ],
    scope: 'energy',
    importFrom: POKEMON,
    importNames: [],
    params: [
      { key: 'holderType', label: 'Holder type', type: 'string' },
      { key: 'count', label: 'Count', type: 'number', defaultValue: 2 },
      { key: 'searchType', label: 'Search type', type: 'string' },
    ],
    patterns: [
      /^when you attach this card from your hand to (?:a|1 of your) (\w+) pok[eé]mon,?\s*search your deck for up to (\d+) basic(?: (\w+))? pok[eé]mon and put them onto your bench\.?\s*then,?\s*shuffle your deck\.?$/i,
    ],
    paramCaptures: { 1: 'holderType', 2: 'count', 3: 'searchType' },
    generateCall: (params, ctx) => {
      const holder = (params.holderType || 'psychic').toLowerCase();
      const search = (params.searchType || holder).toLowerCase();
      const holderId = typeEnumId(holder);
      const searchId = typeEnumId(search);
      const count = num(params, 'count', '2');
      const fn = effectFnName(ctx.powerName || ctx.attackName || 'on_attach');
      const searchLabel = titleCase(search);
      return {
        lines: [fn],
        effectExpr: fn,
        helpers: [
          `async def ${fn}(ctx):\n    types = ctx.attached_to.get_attribute(AttrID.POKEMON_TYPES) or []\n    if PokemonTypes.${holderId}.value not in types:\n        return\n    space = BENCH_CAPACITY - len(ctx.my_bench())\n    take = min(${count}, space)\n    if take <= 0:\n        return\n    picks = await ctx.search_deck(\n        lambda c: is_basic_pokemon(c) and PokemonTypes.${searchId}.value in (\n            c.get_attribute(AttrID.POKEMON_TYPES) or []),\n        count=take, minimum=0,\n        prompt=${JSON.stringify(`Choose up to ${count} Basic ${searchLabel} Pokémon to put onto your Bench.`)},\n    )\n    for card in picks:\n        await ctx.bench_pokemon(card)\n    await ctx.shuffle_deck()\n`,
        ],
        imports: [
          { module: ATTR, names: ['AttrID', 'PokemonTypes'] },
          ...imp('spirit.game.session.effects', 'is_basic_pokemon'),
          { module: 'spirit.game.session.constants', names: ['BENCH_CAPACITY'] },
        ],
      };
    },
  },
];

export function getPrefabById(id: string): PrefabDefinition | undefined {
  return PREFAB_CATALOG.find(p => p.id === id);
}

export function prefabsForScope(scope: string): PrefabDefinition[] {
  return PREFAB_CATALOG.filter(
    p => p.scope === 'both' || p.scope === scope
  );
}

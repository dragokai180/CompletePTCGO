const PYTHON_RESERVED = new Set([
  'and',
  'as',
  'assert',
  'async',
  'await',
  'break',
  'class',
  'continue',
  'def',
  'del',
  'elif',
  'else',
  'except',
  'finally',
  'for',
  'from',
  'global',
  'if',
  'import',
  'in',
  'is',
  'lambda',
  'nonlocal',
  'not',
  'or',
  'pass',
  'raise',
  'return',
  'try',
  'while',
  'with',
  'yield',
]);

/** Snake_case identifier from an attack, ability, or card title (`Protect Charge` → `protect_charge`). */
export function effectFnName(title: string): string {
  let snake = String(title || '')
    .normalize('NFKD')
    .replace(/[\u0300-\u036f]/g, '')
    .replace(/['\u2018\u2019\u2032]/g, '')
    .replace(/,(?=\d)/g, '')
    .replace(/[^a-zA-Z0-9]+/g, '_')
    .replace(/([a-z0-9])([A-Z])/g, '$1_$2')
    .toLowerCase()
    .replace(/_+/g, '_')
    .replace(/^_|_$/g, '');
  if (!snake) return 'effect';
  if (/^[0-9]/.test(snake)) snake = `_${snake}`;
  if (PYTHON_RESERVED.has(snake)) snake = `${snake}_effect`;
  return snake;
}

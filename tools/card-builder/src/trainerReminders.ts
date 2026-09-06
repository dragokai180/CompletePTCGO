/** Catalog/oracle reminder text that is not a card effect. */

function normalize(text: string): string {
  return text
    .normalize('NFKD')
    .replace(/[\u0300-\u036f]/g, '')
    .replace(/[’‘]/g, "'")
    .replace(/[“”]/g, '"')
    .replace(/Pokémon/gi, 'Pokemon')
    .replace(/\s+/g, ' ')
    .trim();
}

const REMINDER_CLAUSE = [
  /^you may play only 1 supporter card during your turn\.?$/i,
  /^you may play any number of item cards during your turn\.?$/i,
  /^you may play only 1 stadium card during your turn\.?$/i,
  /^you can't have more than 1 ace spec card in your deck\.?$/i,
  /^attach (?:a|this) pok[eé]mon tool to 1 of your pok[eé]mon that doesn't already have a pok[eé]mon tool attached\.?$/i,
  /^this stadium stays in play when you play it\.?$/i,
  /^this card stays in play when you play it\.?$/i,
  /^discard it if another stadium(?: card)? comes into play\.?$/i,
  /^discard this card if another stadium card comes into play\.?$/i,
  /^if (?:a stadium|another card) with the same name is in play, you can't play this card\.?$/i,
  /^\(pok[eé]mon ex, pok[eé]mon v, etc\. have rule boxes\.?\)$/i,
  /^\(damage from attacks is still taken\.?\)$/i,
  /^\(existing effects are not removed\.?\s*damage is not an effect\.?\)$/i,
  /^\(damage is not an effect\.?\)$/i,
];

export function isTrainerReminderText(text: string): boolean {
  const n = normalize(text);
  if (!n) return false;
  if (REMINDER_CLAUSE.some(p => p.test(n))) return true;
  return (
    /^this stadium stays in play when you play it\b/i.test(n) ||
    /^this card stays in play when you play it\b/i.test(n)
  );
}

function stripParentheticalReminders(text: string): string {
  return text
    .replace(/\(\s*pok[eé]mon ex, pok[eé]mon v, etc\. have rule boxes\.?\s*\)/gi, '')
    .replace(/\(\s*damage from attacks is still taken\.?\s*\)/gi, '')
    .replace(/\(\s*existing effects are not removed\.?\s*damage is not an effect\.?\s*\)/gi, '')
    .replace(/\(\s*damage is not an effect\.?\s*\)/gi, '')
    .replace(/\s+/g, ' ')
    .trim();
}

export function stripTrainerReminders(text: string): string {
  const cleaned = stripParentheticalReminders(normalize(text));
  const parts = cleaned
    .split(/(?<=\.)\s+/)
    .map(s => s.trim())
    .filter(Boolean)
    .filter(s => !isTrainerReminderText(s));
  return parts.join(' ');
}

const ENERGY_PROVISION = [
  /^as long as this card is attached to a pok[eé]mon, it provides .+ energy\.?$/i,
];

export function stripEnergyText(text: string): string {
  const cleaned = stripParentheticalReminders(normalize(text));
  const parts = cleaned
    .split(/(?<=\.)\s+/)
    .map(s => s.trim())
    .filter(Boolean)
    .filter(s => !ENERGY_PROVISION.some(p => p.test(s)) && !isTrainerReminderText(s));
  return parts.join(' ');
}

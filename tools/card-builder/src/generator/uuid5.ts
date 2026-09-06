/** UUID v5 (SHA-1) for Spirit card GUIDs — matches Python uuid.uuid5(NAMESPACE_DNS, …). */

const DNS_NAMESPACE = '6ba7b810-9dad-11d1-80b4-00c04fd430c8';

function parseUuid(uuid: string): Uint8Array {
  const hex = uuid.replace(/-/g, '');
  const out = new Uint8Array(16);
  for (let i = 0; i < 16; i++) out[i] = parseInt(hex.slice(i * 2, i * 2 + 2), 16);
  return out;
}

function bytesToUuid(bytes: Uint8Array): string {
  const hex = [...bytes].map(b => b.toString(16).padStart(2, '0')).join('');
  return `${hex.slice(0, 8)}-${hex.slice(8, 12)}-${hex.slice(12, 16)}-${hex.slice(16, 20)}-${hex.slice(20)}`;
}

async function sha1(data: Uint8Array): Promise<Uint8Array> {
  const digest = await crypto.subtle.digest('SHA-1', data as unknown as BufferSource);
  return new Uint8Array(digest);
}

/** Deterministic GUID used by import_set: uuid5(DNS, "spirit.ptcgo." + catalogId). */
export async function spiritGuidForCatalogId(catalogId: string): Promise<string> {
  const ns = parseUuid(DNS_NAMESPACE);
  const name = new TextEncoder().encode(`spirit.ptcgo.${catalogId}`);
  const buf = new Uint8Array(ns.length + name.length);
  buf.set(ns, 0);
  buf.set(name, ns.length);
  const hash = await sha1(buf);
  hash[6] = (hash[6] & 0x0f) | 0x50; // version 5
  hash[8] = (hash[8] & 0x3f) | 0x80; // variant
  return bytesToUuid(hash.slice(0, 16));
}

export function cleanCardName(name: string): string {
  return String(name || '').replace(/[^a-zA-Z0-9]/g, '');
}

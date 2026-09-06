# Spirit Card Builder (local)

Local-only UI for scaffolding Spirit PTCGO Python card scripts using existing factories and similar card scripts from the codebase.

## Run

```bash
cd tools/card-builder
npm install
npm run sync-data              # once (or when you want International catalog updates)
npm run sync-data:jp           # optional: prefetch Limitless Japan set index
npm run generate:implemented-ids
npm run dev
```

Opens at [http://localhost:5174](http://localhost:5174).

## Browse cards

The browse view has **International** and **Japan** tabs.

### International (no live API)

Catalog data comes from a local clone of [PokemonTCG/pokemon-tcg-data](https://github.com/PokemonTCG/pokemon-tcg-data):

1. `npm run sync-data` shallow-clones/updates into `data/pokemon-tcg-data`
2. Vite serves that folder at `/tcg-data/*`
3. Browse series → set → card (or search by name) to pre-fill the generator

Reference art uses the `images.pokemontcg.io` URLs already in that JSON. On **Save**, the large image is downloaded to `spirit/assets/cards/<SET>/<Stem>_<number>.png`.

Unimplemented cards are greyed out in the card grid (implemented IDs come from `implementedCardIds.json`). Regenerate after adding scripts:

```bash
npm run generate:implemented-ids
```

### Japan (Limitless unofficial EN translations)

There is no cloneable English-translated Japanese dump. The Japan tab fetches public Limitless pages (`/cards/jp/…?translate=en&display=full`) via the local Vite server, parses them, and caches JSON under `data/limitless-jp/` (gitignored).

- `npm run sync-data:jp` caches the set index. Opening a set (or `npm run sync-data:jp -- --series Mega`) fetches that set’s cards.
- Catalog ids are `jp-{SET}-{number}` (e.g. `jp-M3-21`). Japanese collector numbers often differ from English.
- Known JP→Spirit set twins (`M3`→`ME3`, `M5`→`ME5`, …) fill **Spirit set**; the Japanese number is kept. International prints from Limitless are shown as a hint only.
- Implemented greying matches trainers by name in the mapped Spirit folder. Pokémon match reprint identity first, then the same display name in that folder (Limitless attack names often differ from official English).
- Card text is an unofficial Limitless translation and may differ from later official English, so prefab matching can miss.

Do not commit the Limitless cache.

## Generation rules

- Attack, Ability, and Trainer effect text uses a matching Spirit factory prefab when available (`draw_attack`, `condition_attack`, `flip_damage`, `snipe_attack`, `heal_item`, `search_to_hand`, `professors_research`, `ignore_effects_attack`, `luminous_sign`, …). Evolve Abilities (`When you play this Pokémon from your hand to evolve…`) emit `trigger=Triggers.ON_EVOLVE` rather than `ONCE_PER_TURN`. Play-from-hand Bench Abilities emit `Triggers.ON_PLAY`. SV Mega Evolution Pokémon without `evolvesFrom` are Basic (never both Basic and Stage 1). Special Energy provision sentences (`As long as this card is attached…`) are stripped so remaining on-attach and shield text can match. Stadiums with a continuous cost/counter shield emit `passive=` instead of `effect=unimplemented`.
- If no prefab matches, the builder searches existing scripts under `spirit/game/scripts/cards/**` for a strong same-kind `game_text` match and reuses that `effect=` expression (plus helpers/imports when possible). Copied helper functions are renamed to the new attack, ability, or card title (`Leaf Guard` / `leaf_guard` → `Protect Charge` / `protect_charge`), and helper docstrings are updated to this card's damage and text. Reuse is rejected when numbers, Energy types, named Pokémon, or constraints (`Fusion Strike`, `until you have`, Weakness/Resistance, …) do not match, and truncated `effect=` expressions are skipped.
- Trainer cards also split effect text into clauses, match each clause against factories and other trainers, and stitch those pieces into one named helper when needed. Shared trainer factories in `spirit/game/card_effects/trainers.py` (Ultra Ball, Professor's Research, Switch, …) are part of that corpus. Stadiums that place counters on benched Pokémon emit `abilities=` with `Triggers.ON_POKEMON_BENCHED`.
- If a trainer has the **exact same display name** as an already-implemented script in any set/format, the builder offers a `reprint()` stub. Trainers auto-select reprint; the source may live in another set folder (`sibling_card(__file__, "../SWSH9/UltraBall_150.py")` plus `set_code=` / `key=`).
- Pokémon are **never** offered as reprints based on name alone. A Pokémon reprint is only suggested when an existing script is identical in HP, type, stage, evolves-from, retreat, weakness, resistance, attacks, and abilities. Set, collector number, rarity, and art may differ (same-set alt arts and true reprints).
- If neither a prefab nor a sufficiently similar script is found, text is preserved with `effect=unimplemented`.
- Empty attack text (damage-only) emits no `effect`.
- Output is a Python `*CardDef` script aligned with `spirit/tools/import_set.py` conventions (GUID via `uuid5(DNS, "spirit.ptcgo." + catalogId)`).

## Prefab UI

For each attack, ability, or Trainer effect:

1. Enter effect text and click **Match from text**, or
2. Manually **Add** a prefab from the dropdown and edit parameters.

Then click **Generate card** and copy the Python output.

## Save / new sets

Saving a card:

1. Writes the Python script under `spirit/game/scripts/cards/<SET>/`
2. Downloads art to `spirit/assets/cards/<SET>/`
3. If `<SET>` is missing from `sets.json`, registers it (block, externalId/ptcgoCode, count) and adds it to the appropriate entries in `formats.json` (Expanded always; Standard for modern SV/SWSH-era sets; Legacy for BW)

Existing files require confirmation before overwrite.

## Reprints

**Trainers** with the same display name as an already-implemented script — in this set or another format — can be saved as a Spirit `reprint()` stub.

**Pokémon** are only treated as reprints when the printing is identical besides set, number, rarity, and art (same HP, type, stage, retreat, weakness/resistance, attacks, and abilities). A different Pikachu that shares a name is generated as a full card.

When reprinting, enable **Save as a Spirit reprint() stub** to emit:

```python
from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SWSH9/UltraBall_150.py"),
               collector_number=..., rarity=...,
               set_code="SV09", key="SV09")
```

Same-set secret rares still use a local sibling filename with no `set_code` override.

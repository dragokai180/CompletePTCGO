# Generic text and reprint follow-up

Date: 2026-09-17

## Confirmed and corrected

- **Flare Witch (Delphox BREAK, XY10 14):** the Fire-Energy search branch
  attached correctly but also placed an unprinted damage counter. That
  secondary action now requires the printed clause and a successful
  attachment. This preserves Flare Navigate's counter without adding it to
  Flare Witch; the search remains optional and the deck is shuffled.
- **Sinister Surge (Toxtricity, MEP 17):** the generic deck-attachment branch
  offered every friendly Pokemon and omitted the two damage counters.
  The promo now shares ME2 68's effect and legality predicate. Both printings
  require a Darkness Pokemon on the Bench and a nonempty deck, without
  inspecting the private deck for a matching Energy. Counters are placed
  only after a successful attachment and are not attack damage.
- **Excited Heal (Ludicolo, ME2 7):** its generic permission gate omitted
  the friendly Grass Mega Evolution Pokemon ex requirement. It now checks
  a modern Mega ex in play and its current type, not an opposing Pokemon,
  a Pokemon in hand, or a legacy Mega EX.
- **Solar Transfer (Mega Venusaur ex, MEP 13):** the generic parser supplied
  no Energy predicate for the `Basic Grass` wording, permitting any Energy.
  The promo now shares ME1 3's effect and condition. The generic movement
  parser also preserves the Basic qualifier and type for future imports.
- **Lunar Cycle (Lunatone, MEP 4):** could be activated without Solrock and
  lacked its shared once-per-turn key. It now shares ME1 74's effect and
  permission predicate, including the Basic Fighting Energy payment.
- **Named per-turn limits:** imported abilities with `You can't use more
  than 1 ... Ability each turn` only had a per-card activation flag. The
  normalizer now sets the shared key used by the existing action validator
  and executor. This also covers **Run Errand** (MEP 25), **Cat Walk**
  (SM10 149), and **Quick Search** (SV3 164), including inherited printings.

## Validation

Final full regression run: **991 tests passed**, including 11 new directed
tests in this follow-up. `git diff --check` reported no whitespace errors.

`tests/test_generic_text_regressions.py` checks complete positive and negative
outcomes: attachments without extraneous damage, eligible targets, failed
attachments, deck-empty vs. private search failure, Energy type and Basic
qualifiers, required Pokemon in play, and shared limits across copies.

The preceding discovery pass exercised 523 ability families, 377 Trainer
families, and 336 Mega-era attack families, then used directed probes to
separate real defects from fixture omissions. Dimension Transfer worked with
an Item explicitly placed in the discard pile; Grand Wing correctly affected
the opponent. Neither was changed. An exact-text comparison of generic and
bespoke callbacks identified the additional promo discrepancies above.

This is a targeted follow-up, not certification that every generic clause or
every reprint is correct. Merely observing a draw, attachment, or coin flip is
not proof that all printed requirements and subsequent clauses resolved.

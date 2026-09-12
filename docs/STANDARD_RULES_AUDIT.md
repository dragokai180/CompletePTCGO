# Standard rules audit

Date: 2026-09-12

## Scope and method

This pass uses the project's configured Standard pool (H/I/J), not an
independent certification of current organized-play legality. The configuration
was not changed.

The execution sweep covers SV05, SV06, SV065, SV07, SV08, SV085, SV09, SV10,
RSV10PT5, ZSV10PT5, SVP, ME1, ME2, ME2PT5, ME3, ME4, ME5 and MEP.
Free_Energy contains no executable effect callbacks for this sweep.

Semantic review focused on Trainer permissions, attachment allocation, Special
Energy values and scope, prize reduction, ex/EX distinctions and conditional
switching. This is a broad execution audit plus targeted semantic regression
testing, **not an exhaustive semantic certification of every printed effect**.

## Reproduced and corrected

- **Spikemuth Gym:** its ability supplied a source argument to the two-argument
  deck condition and raised TypeError. The shared deck predicate now accepts
  the optional source while retaining compatibility with Trainer calls.
- **Maximum Belt / Cyrano:** their rules target lowercase Pokemon ex, not
  uppercase Pokemon-EX. They no longer use the helper that combines both eras.
- **Secret Box:** requires a nonempty deck in addition to three other hand
  cards. A nonempty deck with no matching search result remains searchable.
- **Reboot Pod:** players choose which Future Pokemon receive which Energy.
  It no longer assigns selected Energy by board order; each recipient is used
  once, including when there are fewer Energy cards than Future Pokemon.
- **Legacy Energy:** once-per-game usage is tracked separately for each player.
  A knockout must involve attack damage; an attack that only places counters
  does not activate its prize reduction.
- **Neo Upper Energy:** only modifies its own physical Energy card, not other
  attached Energy. Its two provided units may be different types.
- **Ignition Energy / recent Prism Energy:** only modify their own card. Their
  Mega Evolution reprints share the corrected callbacks.
- **Prime Catcher / shared Guzma callback:** the player's switch requires the
  opponent's switch to succeed, respecting the printed conditional sequence.

## Tests

`tests/test_standard_rules_audit.py` adds 11 regression methods with multiple
subcases, including reprints and both ex categories.

`python -m unittest discover -s tests`: **395 tests passed**.

The initial execution sweep found one error (Spikemuth Gym), 4,675 passing
cases and 73 skips. The final sweep completed with **4,676 passing cases,
73 skips and no execution errors or unimplemented callbacks reported**.
The 73 skipped cases still require suitable scenarios and are not approvals.

## Limits

- A passing smoke case means the exercised callback completed without error;
  it does not prove all effects, choices and edge cases were semantically correct.
- The smoke fixture skips actions whose prerequisites are absent. Skips are
  not counted as passes.
- The existing discovery helper enumerates GUID-bearing scripts. Import-only
  reprint modules are not all independently counted. Selected Energy reprints
  have explicit regression coverage.
- No native-client animations, foil rendering or multiplayer UI were tested.
- No server restart or GitHub push was performed.

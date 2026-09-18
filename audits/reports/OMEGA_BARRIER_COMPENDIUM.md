# Omega Barrier: Compendium interaction tests

Date: 2026-09-18. The test-only follow-up confirmed four problems; all four
were corrected after the user's subsequent request.

Source: [Omega Barrier rulings](https://compendium.pokegym.net/category/4-abilities/omega-barrier/).
All seven entries on the supplied category page were read. The web reader
returned HTTP 403, but a direct public HTTP request returned the full articles.

## Results

The original eight test methods cover 21 scenarios, including unprotected
controls. Initially 13 scenarios passed and eight failed, grouped into four
problems. All 21 now pass. Three additional test methods check invalid/stale
Tool targets, ordinary Tool permissions and player-effect scope cleanup.

| Interaction | Expected distinction | Result |
| --- | --- | --- |
| Avery | Player-directed discard bypasses Barrier | PASS with and without Barrier |
| Cyrus Prism Star | Player-directed shuffle bypasses Barrier | PASS with and without Barrier |
| Target Whistle | Trait is inactive in the discard pile | PASS |
| Captivating Poke Puff | Trait is inactive in the hand | PASS with and without Barrier |
| Lysandre | Shield applies to the selected Benched target | PASS in all four Active/Bench combinations |
| Escape Rope | Shield applies to the outgoing Active | PASS in all four Active/Bench combinations |
| Team Flare Tool F | Tools may attach to the opposing Pokemon-EX | PASS for Head Ringer and Jamming Net, with and without Barrier |
| Tool F passive controls | Barrier does not suppress attached Tool effects | PASS for attack-cost increase and damage reduction |

## Reproduced defects and corrections

### Avery

Selecting protected Regirock from a five-Pokemon Bench previously left all
five Pokemon in play. Avery now scopes the discard as an instruction to the
opponent: Pokemon-targeted shields do not block it, but player-wide shields
remain effective. Full stacks enter the discard pile. A no-progress guard
prevents repeating the selection when a player-wide shield blocks movement.

### Cyrus Prism Star

The opponent previously selected two survivors correctly, but the protected
third Pokemon and its Energy remained on the Bench. Cyrus now uses the same
player-directed scope as Avery; the unselected stack enters the deck. Tests
satisfy the Water/Metal Active prerequisite and verify the chooser's identity.
The scoped context is restored after normal completion and exceptions.

### Escape Rope

The shared switch primitive previously checked only the incoming Benched
Pokemon. Escape Rope now explicitly checks the outgoing Active and skips the
opponent's choice when that Active is protected. The acting player's own switch
still resolves. Lysandre retains its distinct incoming-target protection.

### Head Ringer / Jamming Net

Legal actions previously listed the acting player's Pokemon, even non-EX
Snivy, instead of opposing Pokemon-EX. Menu generation and attachment execution
now share target validation: opposing uppercase EX only, with no existing
Tool. Modern lowercase ex, own EX and occupied theta Double holders are
excluded. Execution also rejects a stale target whose Tool slot changed.
Ordinary Tools still target only the acting player's Pokemon. Separate
controlled attachment tests verify Head Ringer's attack-cost increase and
Jamming Net's damage reduction without suppression by Barrier.

## Reproduction and limits

Run from the repository root:

```text
python -m unittest tests.test_omega_barrier_compendium -v
```

All 11 test methods pass. The original failed assertions are retained as
regressions. Production definitions, movement, card effects and legal actions
are exercised; selection UI and the Poke Puff hand viewer are substituted.
These are server-engine tests, not graphical-client or animation tests, and
do not constitute an audit of every Tool F lifecycle interaction.

Full regression: `python -m unittest discover -s tests -q` completed with
1,295 tests passing in 143 seconds (exit status 0).

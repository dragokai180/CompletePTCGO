# All-card execution and effect audit

## Scope

This campaign revisited **every registered printing**, not just the cards named
in earlier bug reports: 15,013 unique card GUIDs across 99 set codes. Basic
Energy attachments, attacks, activated and triggered Abilities, Trainers,
Tools, Stadiums, special rules and continuous effects are included.

This is an automated, headless engine audit. Successful execution is not proof
of every combination with the other 15,012 cards. Runtime checks, text-operation
checks and outcome regressions are separate evidence levels. This is not a
manual client playthrough.

## Confirmed corrections

| Card or effect | Defect and correction |
| --- | --- |
| Kingdra — Dragon Vortex | Count the union of Water/Lightning cards in discard, deal the corresponding damage and shuffle those exact cards. Previously the compound count and shuffle were missed. |
| Snivy — Growth; Unfezant — Tailwind | Accept Energy wording without the word “card”; attach exactly one selected Energy to the printed recipient. |
| Yamask — Astonish | Recognize “a card at random” as well as “a random card”; preserve the coin condition. |
| Carnivine — Spit Squall | Recognize historical Defending Pokemon / his or her hand wording and return the entire defending stack. |
| Honchkrow — Whirlwind | Recognize Defending Pokemon wording, preserve the optional switch and let the opponent select the replacement. |
| Gothitelle — Doom Decree | Apply the Knock Out only on two heads. All four coin combinations have outcome coverage. |
| Donphan — Wreck | Discard the Stadium after applying the bonus; the separate discard sentence was missed. |
| Wild Growth; Burn Brightly; Energy Factory | Stop recursively querying the same resolved Energy provider inside its callback. Transform incoming options while preserving ownership and nonstacking rules. |
| Reboot Pod | Separate the Energy descriptor from Future Pokemon recipients and the ACE SPEC reminder, which incorrectly blocked valid plays. |
| Surfer | Remove the incorrect Water-only switch restriction and implement the missing draw to five after a successful switch. |
| Raticate — Transfer Junk | Recover one Team Plasma Pokemon, Trainer and Energy when available; previously no recovery occurred. |
| Imittack; Copy Anything | Resolve the copied attack using the correct opposing pool and enforce its explicitly required effective Energy cost. |

Shared implementations also apply the corrections to reprints.

## Coverage and evidence

- All-printings ledger: 28,296 printing/behavior/coin scenarios. Early failures
  and skipped conditions were investigated and retested, not silently accepted.
  No card condition or effect was replaced with unconditional success.
  The final clean run, all-printings-verified.jsonl, contains **28,296 PASS**,
  covering all 15,013 GUIDs, with **zero skipped, unplanned or failed probes**.
- Text-family checks: 5,469 attack families, 520 activated/triggered Ability
  families and 377 Trainer families.
- Passive callback sweep: 1,136 implementation/text/state families; 92,410
  initial hook/scope probes plus 1,022 retests, with no unresolved runtime
  failures after retesting. Synchronous hooks exercise both owners;
  asynchronous callbacks receive isolated boards.
- Printed-data comparisons: all 12,544 registered Pokemon printings, with zero
  mismatches, unmatched records or catalog identity collisions. Comparisons
  include HP, stage, lineage, attacks, costs, damage, abilities, Weakness,
  Resistance and Prize values where supplied by the reference records.
  The original local catalog supplied 126 recent promo records absent from
  the local API snapshots.
- Fifteen new focused regression methods assert outcomes. Additional branches
  cover Improvisational Performance at different hand sizes, both Puzzle of
  Time modes, three distinct Eevee-evolution types, failed copy costs and
  nonmatching discard cards.
- Full regression suite after the fixes: **1,193 tests passed**.

### Heuristic alerts that are not defects

Two final broad trace alerts remain visible rather than being whitelisted:

- Eevee's Signs of Evolution uses filtered selection, revealed hand movement
  and shuffle rather than the search_deck convenience method. The outcome
  test checks three types and excludes duplicate types.
- Puzzle of Time's default single-copy run reorders the deck, without recovery.
  Its double-copy regression verifies recovery and payment of the second copy.

The static passive classifier maps all 789 generic text families. Its 141
high-risk labels identify conditional/nonstacking/optional rules; they are not
execution failures or proof that every branch has been verified.

## Reproduce

From the repository root with the configured Python environment:

~~~powershell
python -m spirit.tools.catalog_campaign --jsonl audits/results/all-printings-verified.jsonl
python -m spirit.tools.semantic_effect_audit --kind attack --json audits/results/all-cards-attack-final.json --only-problems
python -m spirit.tools.semantic_effect_audit --kind ability --json audits/results/all-cards-ability-final.json --only-problems
python -m spirit.tools.semantic_effect_audit --kind trainer --json audits/results/all-cards-trainer-final.json --only-problems
python -m spirit.tools.passive_hook_campaign --json audits/results/all-passive-hooks.json
python -m spirit.tools.audit_card_contracts --json audits/results/all-card-contracts.json
$env:PYTHONPATH='tests;.'
python -m unittest discover -s tests -q
~~~

audit_card_contracts accepts --external-catalog-dir to supply original local
catalogs for recent promo records absent from API snapshots. Without these
optional references, the tool reports unmatched records; their runtime tests
are still executed.

Generated JSON/JSONL evidence stays under ignored audits/results/. Both new
campaign tools accept --retry-report without erasing the original evidence.

## Boundaries

This pass does not exercise graphical animations, remote-client timing or all
legal board-state permutations. Hook coverage does not establish that every
conditional effect fired. Focused assertions provide stronger evidence for
the listed defects; the existing suite supplies additional semantic coverage.

No account data, local-only rewards, artwork or foil configuration was changed
by these fixes. Nothing was committed or pushed as part of this request.

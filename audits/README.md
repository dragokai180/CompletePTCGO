# Audits

This folder collects the project's audit reports and local investigation results.

- `reports/`: versioned review summaries, known limitations and test coverage.
- `results/`: generated JSON output and raw investigation notes; local-only
  and ignored by Git. Existing files retain their original names.

## Reports

- [Lost Zone destinations, payments and damage](reports/LOST_ZONE_AUDIT.md)

- [Mandatory costs, Mega ex evolution and attack-effect shields](reports/MODERN_COSTS_AND_EFFECT_SHIELDS.md)
- [Interpreter transactions, conditions and quantities](reports/INTERPRETER_TRANSACTION_AUDIT.md)

- [HeartGold & SoulSilver](reports/HGSS_RULES_AUDIT.md)
- [Black & White](reports/BW_RULES_AUDIT.md)
- [XY](reports/XY_RULES_AUDIT.md)
- [Standard format](reports/STANDARD_RULES_AUDIT.md)
- [Trainer follow-up](reports/TRAINER_FOLLOWUP_AUDIT.md)
- [Full-catalog semantic audit](reports/FULL_CATALOG_SEMANTIC_AUDIT.md)
- [Generic text and reprint follow-up](reports/GENERIC_TEXT_AND_REPRINT_FOLLOWUP.md)
- [Generic conditional clauses and KO reactions](reports/GENERIC_CONDITIONAL_CLAUSES.md)
- [Deck searches and Ability suppression](reports/SEARCH_AND_ABILITY_SUPPRESSION_AUDIT.md)
- [Sun & Moon / Sword & Shield](reports/SM_SWSH_RULES_AUDIT.md)
- [Sun & Moon / Sword & Shield follow-up coverage](reports/SM_SWSH_AUDIT_COVERAGE.md)

## Tools and tests

Executable audit tools stay in [spirit/tools](../spirit/tools/) to preserve
their Python module paths. Regression tests stay in [tests](../tests/) for
standard test discovery. Neither directory was moved.

Run commands from the repository root. On a fresh checkout, first create the
ignored results directory:

```text
python -c "from pathlib import Path; Path('audits/results').mkdir(parents=True, exist_ok=True)"
python -m unittest discover -s tests
python -m spirit.tools.audit_sm_swsh_runtime --json audits/results/sm-swsh-runtime.json
python -m spirit.tools.semantic_effect_audit --kind ability --json audits/results/ability.json
```

Use `--json audits/results/<report-name>.json` when saving other audit runs.
Do not commit raw results, account data, logs, artwork or extracted bundles.

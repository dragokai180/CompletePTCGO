# Robo Substitute and Despair Ray

## Corrections

- Added an explicit `is_rule_action` classification for clickable printed
  removal rules. Robo Substitute, Lillie's Poke Doll, Snorlax Doll and the
  shared fossil-discard action no longer count as Pokemon Abilities.
- These actions remain selectable under Ability suppression and do not send
  an Ability activation banner. Movement, attachment disposal and replacement
  of an empty Active Spot still use the normal resolution pipeline.
- Actual fossil Abilities remain suppressible. Reprints preserve the rule
  action classification.
- Despair Ray previously added its chosen-discard bonus AND a generic bonus
  for the remaining Bench. The generic formula no longer interprets
  "Benched Pokemon you discarded" as the current Bench population.

## Regression coverage

`tests/test_robo_substitute_despair_ray.py` exercises:

- Robo Substitute in the Active Spot and on the Bench under a turn-scoped
  Ability lock, Silent Lab and Garbotoxin.
- Attached-card disposal, no Prize award, replacement Active and no Ability
  announcement for voluntary removal.
- The corresponding Doll/fossil rules without exempting real Abilities.
- Both Despair Ray printings, discarding zero, one or three Pokemon: 110,
  120 or 140 base damage respectively, regardless of the remaining Bench.

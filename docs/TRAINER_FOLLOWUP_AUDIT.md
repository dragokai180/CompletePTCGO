# Trainer follow-up audit

Date: 2026-09-13

This targeted semantic pass starts from Rough Seas and Evosoda and reviews
related healing Stadiums and deck-evolution Trainers. It is not a completed
audit of every Trainer in the game.

## Reproduced and corrected

- Rough Seas: requires an injured Water or Lightning Pokemon belonging to
  the activating player. Resolves healing on every eligible Pokemon, not
  on the opponent's board or unrelated types.
- Evosoda, including Generations: explicitly searches for the chosen
  Pokemon's direct evolution and evolves it from the deck. No skipping
  stages. Requires a nonempty deck and a target from a previous turn;
  cannot be played on either player's first turn. Evolution locks are
  respected. Hidden absence of an evolution does not prevent play, and
  searches can fail and still shuffle.
- Life Forest: requires an eligible Grass Pokemon with damage or a Special
  Condition. Can remove conditions even at full HP, and cures all of them.
- All-Night Party: requires an Asleep Active, not just an injured Active.
  Removes Sleep and heals 30.
- Wally, including its shared reprint: cannot be played with an empty deck.
  Its existing first-turn and newly-played-Pokemon exceptions are retained.
- Pokemon Breeder's Nurturing (166, 188, 195): requires a nonempty deck and
  a timing-eligible, evolution-unblocked target. The selection limit is
  bounded by the number of candidates. Does not inspect hidden matches.
- Celebratory Fanfare: requires damage to heal; ends the turn only when
  some damage was actually healed.

The healing Stadiums share an explicit target predicate between permission
and resolution. Other continuous Stadium rules remain in their existing
passives.

## Validation and limits

Eight new regression methods in tests/test_trainer_followup_audit.py cover
the reported outcomes and related permissions, including reprints, opposing
ownership, types, turn timing, and private deck information. They exposed
failures before the fixes.

Full suite: 414 tests passed. Existing SQLite ResourceWarnings remain.
No multiplayer client/animation validation was performed. Further Trainer
families and combinations still need outcome-level review.

No commit, push, or server restart was performed in this pass.

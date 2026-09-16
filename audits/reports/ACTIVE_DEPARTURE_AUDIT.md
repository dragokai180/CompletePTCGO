# Active Departure and Replacement Audit

## Scope

Shared attack, Ability and Trainer flows that remove or replace an Active
Pokemon: hand/deck return, discard/Lost Zone departure, Knock Out, switching
to the Bench, and simultaneous empty Active spots. This is an engine-flow
audit, not a claim that every individual card has been replayed in the UI.

## Reproduced failure

The local client log at 23:38 on September 15 reported:
`Couldn't find group animator ... Indeck, deckHit, GroupedMove`.
The installed client's PlaceDamageEffect executor (m.p) chooses its hit
animation from the target's current area. It cannot animate damage in a deck.

Deck and Cover reproduced stale retaliation from Rough Skin (Druddigon),
Horror Psychic Energy and Rocky Helmet. Accelgor was already in its deck,
but its reset 90 HP became 70 and the server emitted a damage animation there.
The animation queue then stopped before the otherwise-valid promotion offer.

## Shared corrections

- Damage, healing, direct Knock Out, Special Conditions and counter movement
  require a top-level in-play Pokemon, not merely a registered entity ID.
- Deferred retaliation revalidates its original attacker; it never redirects
  damage to the replacement Active. A switched attacker still on the Bench
  remains a valid damage target.
- Deferred lethal retaliation flushes damage choreography before KO movement,
  Prize selection and promotion. This covers generic text reactions, typed
  retaliation and Horror Psychic Energy.
- KO settlement ignores stale references to cards that already left play.
- Return-to-hand stack movements are tagged as follow-up GroupedMove runs;
  they no longer ride inline inside the Attack bracket and remove its source
  while that animation is executing.
- Attacks use the same empty-Active settlement as Abilities and Trainers,
  including non-turn-player-first order for simultaneous departures.
- An on-damage trigger that changes nothing does not announce a false activation.

## Regression coverage

`test_active_departure_audit` exercises real Deck and Cover with three reaction
families and no reaction, both owners, the human choice of the second Benched
Pokemon, automatic single replacement, loss with no replacement, simultaneous
departures, valid Bench retaliation, lethal retaliation message ordering,
stale targets in four out-of-play zones, and full-stack hand return after the
attack animation. Its message checker tracks native EntityMoved commands and
rejects a PlaceDamageEffect after its target has left the field.

Existing `test_empty_active_promotion`, `test_lillies_poke_doll_knockout` and
the full regression suite cover the surrounding Trainer/Ability/KO flows.
The client freeze is corroborated by its crash log and decompiled executor,
but the corrected UI still needs a new test after restarting the server.

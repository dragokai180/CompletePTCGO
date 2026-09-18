# Player choice, deck ownership and private views

Date: 2026-09-18

## Scope

Targeted regression audit of 29 card definitions, including Hiker's alternate
printing. Both players are tested as the effect controller and as the selected
owner. Empty decks, a single remaining card, larger decks and expanded Benches
are included. This is server/protocol coverage, not a native-client visual test.

## Confirmed and corrected

- **Hiker (SM7 133, HF 185) / Chip-Chip Ice Axe (SM10 165):** the
  permission check incorrectly required the controller's deck to be nonempty,
  even when the opponent's deck was the target. It now checks the deck(s) named
  in the effect. Hiker offers only nonempty decks. Private inspection, mandatory
  one-card selection, final top card and unchanged other-player deck are tested.
- **Gothita (BW6 55), Reuniclus (BW3 52, BW11 76):** Future Sight
  incorrectly used the opponent's deck rather than its controller's deck.
- **Lunatone (SWSH3 72), Duskull (SWSH4 69), Porygon (SWSH11 140),
  Gothita (SWSH3 73), Orbeetle (SWSH1 19), plus the three BW cards above:**
  manual deck-order implementations did not send the new order to clients.
  They now use the shared private reorder operation, including the one-card
  inspection case. Tests inspect the actual chooser offer and PileReordered
  message: card faces go only to the controller; order messages contain IDs only.
- **Alomomola (SM2 36):** Borne Ashore offered discard cards even if their
  owner's Bench could not receive them, and allowed an optional pick despite
  the mandatory public-zone instruction. The common recovery branch now filters
  valid entry targets and respects the printed quantity and available slots.
- **Mantine (SWSH10 34):** Borne Ashore treated five as the fixed Bench
  capacity. Selection and permission now use the effective capacity and entry
  restrictions; Sky Field is covered on either player's side.
- The shared Trainer reorder clause now honors `either player's` instead of
  silently defaulting to the controller's deck (template regression included).

## Additional effects checked

- Second Sight: Slowking HGSS1 12 and COL 32.
- Future Sight/Future Spin: Celebi HGSS4 3, Baltoy XY7 32, Xatu XY6 29,
  Absol SM2 81, Munna SM11 88, Natu SM12 78 and Absol ex SV3 135.
- Fiddle Around: Aipom XY11 90.
- Trick Shovel XY2 98: private look, optional discard, correct discard owner.
- Sand Flap (Flygon XY5 110), Either Face (Farigiraf SV2 155) and
  Seething Currents (Kingdra SWSH11 37): only the selected player's hand changes;
  Kingdra preserves the existing deck top while placing the old hand underneath.
- Opponent's Choice (Slowking HGSS3 85): the opponent actually chooses; the
  selected card goes to the power user's hand, the other to their deck bottom.
- Trick (Mr. Mime XY5 101): moving either player's Tool retains its owner and
  limits destinations to that owner's other Pokemon.

## Reproduction

Full unittest discovery passed after the corrections (1,217 tests). The checks
exercise server state and protocol messages; native-client visual validation
was not performed.

```text
python -m unittest tests.test_player_choice_effects tests.test_deck_order_privacy -v
python -m unittest discover -s tests -q
```

Regression runs reproduced incorrect permissions, deck ownership, missing order
updates and invalid/full-Bench selections before the fixes. Existing local LEGEND,
Slowking privacy, account and foil changes were preserved. No server restart or
GitHub push is part of this audit.

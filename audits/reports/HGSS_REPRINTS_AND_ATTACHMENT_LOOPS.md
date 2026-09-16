# HGSS reprints and repeatable attachment Abilities

## Expanded legality

Expanded now shares Legacy's printing-independent identity check. Old HGSS
Trainer and Special Energy printings are legal when the configured format
contains an equivalent legal printing, including HGSS Double Colorless Energy.
This does not legalize the entire HGSS era or make Double Colorless Energy legal
in the current Standard format. Explicit bans, source release dates and the
combined four-copy limit still apply. Reprint indexes are cached per format.

## Attachment interaction

Repeatable hand-attachment Abilities use a shared sequence:

1. Select an eligible Energy in hand, or Done.
2. Select an eligible Pokemon in play.
3. Send the attachment movement to both clients without an Ability animation.
4. Resolve attachment observers and recheck the available cards and targets.
5. Repeat; stop on Done or when no eligible attachment remains.
6. After at least one successful attachment, play the Ability animation once.

Coverage includes Inferno Fandango, Deluge, Rain Dance, Magnetic Circuit,
Super Cold, Electric Streamer, Crazy Code, Dark Squall, Ice Dance, Spring
Bloom, Oceanic Accompaniment and Excited Turbo, including their shared reprints.
Single-use powers such as Water Acceleration retain their printed limits.
The loop does not spend the ordinary once-per-turn Energy attachment.

## Regression coverage

- HGSS reprint legality, bans, release dates and mixed-print copy limits.
- Move-before-next-selection ordering and one final Ability announcement for
  both players.
- Done before/after an attachment, exhaustion, type and target restrictions,
  Special Energy, hand attachment observers and single-use powers.

Tests inspect server state and outgoing choreography. Native client animation
playback still needs an in-game visual check after restarting the server.

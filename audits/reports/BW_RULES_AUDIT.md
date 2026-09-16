# Black & White rules audit

Date: 2026-09-12

## Status

The server-side audit pass now covers BW1-BW11, Dragon Vault and BW Promos.
The review compares rules text with shared dispatchers and set-specific
callbacks, then reproduces identified defects with regression tests.
This is not exhaustive branch coverage or native-client visual certification.

## Reproduced and corrected

- Magical Leaf: its healing requires heads, not merely using the attack.
- Fire's Power / Water's Power / Grass' Power: the secondary condition/healing
  requires the specified attached Energy; the base damage remains unconditional.
- Spit Acid: always Burns and additionally Paralyzes on heads. The parser missed
  the word "also" in its second condition clause.
- Final Gambit: recoil only when both coins are tails.
- Zap Cannon: the next-turn attack lock only applies on tails.
- Gyro Ball: switch the attacking player's Pokemon first, then the opponent
  chooses their replacement. Other explicit "opponent switches/chooses" attack
  templates now give that choice to the opponent rather than the attacker.
- Quick Tail Smash: the player can decline the optional coin and retain base
  damage rather than being forced to gamble.
- Energy Wheel: move from the Bench to Tornadus, not the opposite direction.
- Hurricane: moving one basic Energy is mandatory when a target and Energy exist.
- Ether: allow any allied Pokemon as recipient, including the Bench.
- Computer Search: select one card; unrestricted searches cannot fail to find.
  The chosen card remains unrevealed.
- Old Amber Aerodactyl: display all seven viewed bottom cards even if none qualify;
  allow declining the selection, and disallow playing it with a full Bench.
- Black Eyes: require Energy on the opponent's Active as well as Krookodile
  being Active. Recognize the "attached to" wording in the public-target gate.

## Verification

`python -m unittest discover -s tests`: **384 tests passed**. The BW work adds
49 tests across five modules, including positive/negative subcases. The complete
suite includes HGSS and modern-era regressions because the dispatchers are shared.

The final smoke sweep executed **2,392 passing cases**, with no execution errors
or unimplemented callbacks reported among those cases. **20 cases were skipped**
by the generic fixture's legality checks. Fortunate Draw was tested separately
with deterministic choices, including ties and both winning players; an
always-pick-first smoke bot would tie forever.

| Set | Passing smoke cases | Skipped |
| --- | ---: | ---: |
| BW1 | 172 | 1 |
| BW2 | 170 | 0 |
| BW3 | 168 | 2 |
| BW4 | 178 | 0 |
| BW5 | 185 | 1 |
| BW6 | 222 | 1 |
| BW7 | 247 | 2 |
| BW8 | 225 | 2 |
| BW9 | 201 | 1 |
| BW10 | 171 | 6 |
| BW11 | 241 | 1 |
| Dragon Vault | 34 | 1 |
| BW Promos | 178 | 2 |

The skipped fixtures concern Revive, Mysterious Evolution, Dark Patch,
Devolution Spray, Rush In, Colress Machine, Dowsing Machine, Shadow Triad,
G Booster, G Scope, Tool Reversal, Plasma Transfer, Rare Candy and First Ticket
(including alternate prints). First Ticket belongs to pre-game setup, not an
ordinary Trainer action. These skips are **not** passes.

The smoke discovery tool enumerates GUID-bearing scripts; reprints that import
their definition are not separately counted. They reuse callbacks but their
individual metadata is not certified by this sweep. Smoke success only proves
that the exercised path executes; semantic assertions live in the tests below.

## Additional reproduced corrections

- Stadium Drain, Stadium Burn and Stadium Wave require a Stadium for their rider.
- Double Freeze requires at least one heads; multi-coin status clauses respect
  their individual requirements.
- Deep Dive heals per heads; Healing Melody, Sky Heal and Poison Suction respect
  their coin, named-Bench and Poison prerequisites.
- Energy Bloom heals only Pokemon with attached Energy.
- Swift Sting applies its condition only at full HP.
- Captivate respects the coin; Slurp Shakedown and Tractorbeam damage the new
  Active rather than the Pokemon switched out.
- Leaf Tailor requires Energy; Craftsmanship counts provided Fighting Energy
  units; Sealing Scream blocks ACE SPEC cards for both players.
- Slippery Soles lets the opponent choose their own replacement, after the
  activating player's successful switch.
- Le Parfum, Final Wish, Reversal Trigger and Clear Search cannot fail an
  unrestricted search when cards remain. The results remain private.
- Stellar Guidance may search a nonempty deck even when it has no Supporter.
- Burning Wind, Groovy Dance and Flying Beatdown apply their condition only
  after accepting and paying the optional Energy discard.
- Payback and Thunderous Noise discard only when their Prize/Plasma requirement
  is met. Tests cover both valid and invalid states.
- Sand Bazooka permits declining its Energy movement.
- Signs of Evolution selects Eevee evolutions of different types.
- Fortunate Draw resolves Rock-Paper-Scissors, replaying ties, then draws for the
  winner and mills the loser's deck.
- Pokemon Communication reveals the returned Pokemon before searching and
  shuffles only after the search.
- Old Amber reads the bottom seven cards, not the top seven.
- Random Receiver starts at the actual top of the deck.
- Town Map keeps the revealed Prize identities public.

Regression modules:

- `tests/test_bw_rules_audit.py`
- `tests/test_bw_remaining_attacks.py`
- `tests/test_bw_passive_audit.py`
- `tests/test_bw_ability_audit.py`
- `tests/test_bw_trainers_energy_audit.py`

Special Energy assertions cover Double Colorless, both Blend variants, Plasma
and Prism's Basic-Pokemon restriction. Additional assertions cover Dark Aura,
Psychic Mirage, Solar Revelation, Flare Navigate and private top-card choices.
No server restart, GitHub push or native-client visual test was performed.

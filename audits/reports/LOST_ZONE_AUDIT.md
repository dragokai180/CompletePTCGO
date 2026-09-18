# Lost Zone follow-up audit

## Scope

Reviewed the 55 distinct explicit Lost Zone rules texts found in the Python
card catalog, shared movement/KO primitives, and the corresponding authored
Lost Origin effects. Existing tests cover Lost World, Lost Link, Catastrophe,
Lost Out, Lost Vacuum, Prism Star replacement, and Lost Zone attack thresholds.
This is a targeted semantic audit, not proof of every possible combination.

## Corrections

- See Off (Mew Prime): selected Pokemon goes directly from the deck to the
  public Lost Zone, never to hand; failed typed searches still shuffle.
- Lost Crush (Banette): on heads, select an Energy on any opposing Pokemon,
  including the Bench, and move it to its owner's Lost Zone.
- Plow Over (Tangrowth): heads applies Paralysis; tails alone removes an
  Energy. Neither branch removes the attacker's Energy.
- Lost Claw (Zangoose): one random opposing hand card goes to the Lost Zone;
  the rest of that private hand is not revealed.
- Vicious Claw (Absol Prime): move one Pokemon from hand before dealing damage;
  with no Pokemon payment, the attack does nothing.
- Dimension Sphere and Lost March: count only the player's Lost Zone Pokemon.
  Lost March excludes Prism Star Pokemon, including alternate text encodings.
- Unseen Flash: require and move two Lightning Energy cards from hand before
  applying Paralysis; insufficient resources disable activation; declining
  the optional effect pays nothing.
- Lost Boomerang-GX: redirect only Pokemon knocked out by that resolution's
  damage, together with their attachments. Surviving targets stay in play,
  effect immunity is respected, and the replacement does not leak to later
  attacks.
- Lost Impact, Magical Fire, and Lost Flame: count attached Energy value rather
  than requiring two physical cards. Copied attacks still resolve as much as
  possible when fewer Energy are available. Lost Burn still counts physical
  Energy cards, as its text specifies.
- Hurl into Darkness reveals the opposing hand once rather than twice.
- Tightened generic attached-Energy matching to distinguish the attacker from
  the defender and respect the relevant coin clause.

## Regression coverage

See tests/test_lost_zone_audit.py. Tests use real definitions and board moves
for destinations, search failure, coin outcomes, payments, Energy value,
Prism Star exclusions, immunity, KO stacks, and hidden/public zone boundaries.
Existing Comfey and Giratina top-deck splits are also checked.

Validation: all 1,178 tests passed, including 17 Lost Zone regression tests.

Run from the repository root:

    python -m unittest discover -s tests

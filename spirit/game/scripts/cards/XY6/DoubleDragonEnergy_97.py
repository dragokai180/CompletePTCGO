"""Double Dragon Energy (XY - Roaring Skies 97/108).

  "This card can only be attached to Dragon Pokemon. This card provides
   every type of Energy but provides only 2 Energy at a time. (Doesn't
   count as a basic Energy card. If the Pokemon this card is attached to
   is not a Dragon Pokemon, discard this card.)"

Two halves, handled separately:

  attach_to  -- the "can only be attached to Dragon Pokemon" clause, the
                same hook Team Rocket's Energy uses for its own restriction.
                Filters the legal attach targets in legal_actions and is
                re-checked in _execute_attach_energy.
  provides   -- every type, two at a time. attack_cost_satisfied() flattens
                an energy into (union of its option types, longest option),
                so this pays 2 toward a cost and the two halves may answer
                two different type requirements -- which matches the ruling
                that Double Dragon Energy can pay, say, [W][L] on its own.

The trailing "if the Pokemon this card is attached to is not a Dragon
Pokemon, discard this card" clause is discard_if_invalid: attach_to gates
playing the card from hand, and that flag makes the engine re-read the same
predicate after an effect moves or attaches the card, which is how Elgyem's
Slight Shift stops being a way to park this on a Klefki.

Still not covered: a Dragon that stops being a Dragon while the card sits on
it (evolving into a non-Dragon, Kecleon's Chromashift). Nothing re-reads the
restriction on evolution, only on attach and move.

Roaring Skies is registered in sets.json as "XY6" (externalId "ROS"), and
that is the value AutoBundle matches on -- see the note in SM5/DialgaGX_100.py
about "UPR" for why the canonical name, not the externalId, is the set_code.
"""

from spirit.game.card_effects.energies import ALL_TYPES_ONE_AT_A_TIME
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import AttrID, PokemonTypes, Rarities

# Every type of Energy, two at a time. PokemonTypes members (not .value)
# because `provides` is declared in terms of the enum; the passive-side
# constant in SV05/NeoUpperEnergy_162.py holds the int values instead.
ALL_TYPES_TWO_AT_A_TIME = [
    [option[0], option[0]] for option in ALL_TYPES_ONE_AT_A_TIME
]


def _is_dragon(pokemon) -> bool:
    """The printed types, matching how the other type-gated Special Energies
    (Speed Lightning, Heat Fire) read their target."""
    types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.DRAGON.value in types


card = EnergyCardDef(
    guid="2f0c1f4b-b09c-5cb4-9a43-a19803ede03e",
    key="XY6",
    name="Double Dragon Energy",
    display_name="Double Dragon Energy",
    searchable_by=["Double Dragon Energy", "Special", "DoubleDragonEnergy"],
    subtypes=["Special"],
    collector_number=97,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    attach_to=_is_dragon,
    discard_if_invalid=True,
    provides=ALL_TYPES_TWO_AT_A_TIME,
)

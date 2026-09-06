"""Rapid Strike Energy (SWSH - Battle Styles 140/163).

Special Energy.

  "This card can only be attached to a Rapid Strike Pokemon. If this card
   is attached to anything other than a Rapid Strike Pokemon, discard this
   card."
  "As long as this card is attached to a Pokemon, it provides 2 in any
   combination of Water Energy and Fighting Energy."

Team Rocket's Energy with a different pair of types and a different
restriction, so it takes the same shape: three provides options for the
combinations, attach_to for the restriction and discard_if_invalid for
the sentence that enforces it after an effect parks the card somewhere
illegal.

It shipped as a bare one-Colorless stub -- no provides, no restriction --
so it paid a single Colorless to anything.
"""

from spirit.game.data_utils import EnergyCardDef, subtypes_for
from spirit.game.attributes import PokemonTypes, Rarities


def is_rapid_strike(pokemon) -> bool:
    """Rapid Strike is a printed subtype, like Single Strike and Fusion
    Strike. Board entities do not carry subtypes, so it is read off the
    definition -- the same lookup Team Rocket's Energy uses for its own
    restriction."""
    return "Rapid Strike" in subtypes_for(pokemon.archetype_id)


RAPID_STRIKE_PROVIDES = [
    [PokemonTypes.WATER, PokemonTypes.WATER],
    [PokemonTypes.WATER, PokemonTypes.FIGHTING],
    [PokemonTypes.FIGHTING, PokemonTypes.FIGHTING],
]


card = EnergyCardDef(
    guid="73c65f08-c971-5757-aeea-24da7388a716",
    key="SWSH5",
    name="Rapid Strike Energy",
    display_name="Rapid Strike Energy",
    searchable_by=["Rapid Strike Energy", "Special", "Rapid Strike"],
    subtypes=["Special", "Rapid Strike"],
    collector_number=140,
    set_code="SWSH5",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    attach_to=is_rapid_strike,
    discard_if_invalid=True,
    provides=RAPID_STRIKE_PROVIDES,
)

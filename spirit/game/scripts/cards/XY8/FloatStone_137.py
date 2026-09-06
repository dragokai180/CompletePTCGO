"""Float Stone (XY - BREAKthrough 137/162).

Pokemon Tool.

  "The Pokemon this card is attached to has no Retreat Cost."

retreat_free_when with a holder predicate, which is exactly how Magnetic
Metal Energy (ME4 85) does it from an attachment: carrier_pokemon(carrier)
walks up the stack to the Pokemon the card is on, and this one drops that
card's Metal-type test because Float Stone does not care what it is on.

The factory's predicate is free-form -- Latias ex's Skyliner gates on owner
and stage rather than on identity, and Charmander's Agile happens to use
`pokemon is carrier` only because a Pokemon carries its own Ability. There
was no need for a bespoke Passive class here.

Air Balloon's own passive stays hand-written next to it in
card_effects/trainers.py: it subtracts 2 rather than zeroing, so the factory
does not cover it.

The card's other two sentences are the standard Tool and Item rules the
engine already enforces.
"""

from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import retreat_free_when
from spirit.game.session.passives import carrier_pokemon


def _holder(pokemon, carrier) -> bool:
    return carrier_pokemon(carrier) is pokemon


card = PokemonToolCardDef(
    guid="5d073628-31df-5dd0-91f1-df851a226be7",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FloatStone.Name",
    display_name="Float Stone",
    searchable_by=["Float Stone", "Pokémon Tool", "FloatStone"],
    subtypes=["Pokémon Tool"],
    collector_number=137,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    passive=retreat_free_when(_holder),
)

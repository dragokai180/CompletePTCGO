"""Silent Lab (XY - Primal Clash 140/160).

Stadium.

  "Each Basic Pokemon in play, in each player's hand, and in each player's
   discard pile has no Abilities."

The same two hooks Garbotoxin needed, with a different filter and no switch.
blocks_abilities covers the board; blocks_out_of_play_abilities is the one
that reaches hands and discard piles, and it exists because every other lock
in the game reads "Pokemon in play" -- see the note on
_out_of_zone_ability_entries.

Where Garbotoxin has to spare its own kind and only runs while a Tool is
attached, this is a Stadium: always on, no exception clause. Every Basic
loses its Abilities, Klefki's Mischievous Lock included, and Silent Lab
itself is a Stadium passive rather than an Ability so nothing can switch it
off in turn.
"""

from spirit.game.card_effects.trainers import SilentLabPassive
from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    passive=SilentLabPassive(),
    guid="ff59974c-334d-58fb-bd26-96f35695006e",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SilentLab.Name",
    display_name="Silent Lab",
    searchable_by=["Silent Lab", "Stadium", "SilentLab"],
    subtypes=["Stadium"],
    collector_number=140,
    set_code="XY5",
    rarity=Rarities.Uncommon,
)

from spirit.game.data_utils import Activations, reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(
    sibling_card(__file__, "../BW9/Exeggcute_4.py"),
    collector_number=102,
    set_code="BW10",
    key="BW10",
    guid="a0c73251-03d7-5750-9b82-f806ac3a4fa9",
    rarity=Rarities.RareSecret,
)

# Propagation may be repeated while Exeggcute is in the discard pile.  The
# printing's legacy "Once during your turn" wording was later clarified by
# ruling and this server consistently exposes that interaction as unlimited.
card.abilities[0].activation = Activations.UNLIMITED

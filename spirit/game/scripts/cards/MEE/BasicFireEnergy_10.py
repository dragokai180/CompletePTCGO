"""30th anniversary artwork, printed in the Mega Evolution Energy catalog."""
from uuid import NAMESPACE_URL, uuid5

from spirit.game.data_utils import reprint
from spirit.game.scripts.cards.SVE.BasicFireEnergy_2 import card as base_card

card = reprint(
    base_card,
    guid=str(uuid5(NAMESPACE_URL, "completeptcgo:MEE:10")),
    set_code="MEE",
    key="MEE",
    collector_number=10,
    regulation_mark=None,
)

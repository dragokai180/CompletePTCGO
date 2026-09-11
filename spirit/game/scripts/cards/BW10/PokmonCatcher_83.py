from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(
    sibling_card(__file__, "../CZ/PokemonCatcher_138.py"),
    collector_number=83,
    set_code="BW10",
    key="BW10",
    guid="c1507558-3d36-586e-88b8-f9e2ec887693",
    rarity=Rarities.Uncommon,
)

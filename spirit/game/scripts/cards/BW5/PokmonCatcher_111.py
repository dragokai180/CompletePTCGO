from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../CZ/PokemonCatcher_138.py"),
               collector_number=111, rarity=Rarities.RareSecret,
               set_code="BW5", key="BW5")

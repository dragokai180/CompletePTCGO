from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV07/GlassTrumpet_135.py"),
               collector_number=110, rarity=Rarities.Uncommon,
               set_code="SV085", key="SV085",
               regulation_mark="H")

# Gallery print swsh10tg/TG04; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH1.Frosmoth_64 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=220,
    rarity=Rarities.ChrRareHolo,
    guid='59976722-8a73-5a65-84e4-a1120f077d01',
    set_code='SWSH10',
    key='SWSH10',
    regulation_mark='D',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG04"}

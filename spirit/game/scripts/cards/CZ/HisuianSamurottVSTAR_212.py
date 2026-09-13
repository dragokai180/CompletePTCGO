# Gallery print swsh12pt5gg/GG52; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH10.HisuianSamurottVSTAR_102 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=212,
    rarity=Rarities.RareHoloVSTAR,
    guid='999da08a-82bd-5b0c-b730-d8eee75aa0ac',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG52"}

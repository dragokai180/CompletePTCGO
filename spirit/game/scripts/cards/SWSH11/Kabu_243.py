# Gallery print swsh11tg/TG26; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH3.Kabu_163 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=243,
    rarity=Rarities.RareUltra,
    guid='929f74cf-e507-52a4-b677-35b98feedaed',
    set_code='SWSH11',
    key='SWSH11',
    regulation_mark='D',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG26"}

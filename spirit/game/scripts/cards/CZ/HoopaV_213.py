# Gallery print swsh12pt5gg/GG53; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH8.HoopaV_253 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=213,
    rarity=Rarities.RareHoloV,
    guid='46f7a635-ee46-5d29-967b-c908de81c132',
    set_code='CZ',
    key='CZ',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG53"}

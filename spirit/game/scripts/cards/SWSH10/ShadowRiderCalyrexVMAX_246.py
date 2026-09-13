# Gallery print swsh10tg/TG30; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH6.ShadowRiderCalyrexVMAX_75 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=246,
    rarity=Rarities.RareSecret,
    guid='c75aeba1-e5e3-588d-9a74-773ba7f7fcc4',
    set_code='SWSH10',
    key='SWSH10',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG30"}

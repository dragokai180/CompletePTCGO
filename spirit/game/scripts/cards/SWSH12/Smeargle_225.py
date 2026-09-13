# Gallery print swsh12tg/TG10; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH12.Smeargle_137 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=225,
    rarity=Rarities.ChrRareHolo,
    guid='e122ca97-b69b-59e3-9092-495cd888dfa4',
    set_code='SWSH12',
    key='SWSH12',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG10"}

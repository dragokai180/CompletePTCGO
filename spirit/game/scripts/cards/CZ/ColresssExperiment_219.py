# Gallery print swsh12pt5gg/GG59; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH11.ColresssExperiment_155 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=219,
    rarity=Rarities.RareUltra,
    guid='a6895b89-8339-556b-928e-3fa74f80407d',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG59"}

from spirit.game.scripts.cards.ME55.Mew_65 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=161,
    rarity=Rarities.Common,
    guid='783421a9-1359-55c1-8075-b60011166f1b',
    set_code='ME55',
    key='ME55',
    regulation_mark='J',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'B'}

from spirit.game.scripts.cards.ME55.Mew_65 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=159,
    rarity=Rarities.Common,
    guid='68c82dfd-9afe-56e3-982f-2cbc73bd08d6',
    set_code='ME55',
    key='ME55',
    regulation_mark='J',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'R'}

from spirit.game.scripts.cards.SWSH10.KleavorV_87 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=248,
    rarity=Rarities.RarePromo,
    guid='ebc2b6fd-826f-5dac-9a76-524be0f2e3c6',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH248'}

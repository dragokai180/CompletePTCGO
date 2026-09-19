from spirit.game.scripts.cards.SWSH10.VirizionV_164 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=295,
    rarity=Rarities.RarePromo,
    guid='4ff30cdb-dd01-5f5d-acb3-89df496a702c',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH295'}

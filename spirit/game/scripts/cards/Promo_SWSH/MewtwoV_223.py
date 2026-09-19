from spirit.game.scripts.cards.PGO.MewtwoV_30 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=223,
    rarity=Rarities.RarePromo,
    guid='ecdaacc7-d8c5-5717-bc67-e4677a7be208',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH223'}

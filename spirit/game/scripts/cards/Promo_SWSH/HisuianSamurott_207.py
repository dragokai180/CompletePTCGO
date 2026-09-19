from spirit.game.scripts.cards.SWSH10.HisuianSamurott_100 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=207,
    rarity=Rarities.RarePromo,
    guid='41a264a7-f51c-585d-8163-7dc998965126',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH207'}

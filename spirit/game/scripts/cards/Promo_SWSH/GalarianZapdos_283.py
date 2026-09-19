from spirit.game.scripts.cards.SWSH7.GalarianZapdos_82 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=283,
    rarity=Rarities.RarePromo,
    guid='5c062305-c30f-536f-8859-909c8d55fb76',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH283'}

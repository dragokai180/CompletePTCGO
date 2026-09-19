from spirit.game.scripts.cards.SWSH2.DragapultVMAX_93 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=97,
    rarity=Rarities.RarePromo,
    guid='10624b65-5ca6-5e7f-ade1-889c04f6352b',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH097'}

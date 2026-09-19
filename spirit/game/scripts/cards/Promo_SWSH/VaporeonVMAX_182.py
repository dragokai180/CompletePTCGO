from spirit.game.scripts.cards.SWSH7.VaporeonVMAX_30 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=182,
    rarity=Rarities.RarePromo,
    guid='7eef8897-ed3c-5515-a304-1c9a89499301',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH182'}

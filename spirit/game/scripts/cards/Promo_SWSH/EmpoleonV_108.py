from spirit.game.scripts.cards.SWSH5.EmpoleonV_40 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=108,
    rarity=Rarities.RarePromo,
    guid='b308d586-bf91-5231-9e96-b53da987eafb',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH108'}

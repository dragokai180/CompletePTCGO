from spirit.game.scripts.cards.PGO.MelmetalV_47 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=224,
    rarity=Rarities.RarePromo,
    guid='c59938bc-b475-5799-af97-23fb1d29bf25',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH224'}

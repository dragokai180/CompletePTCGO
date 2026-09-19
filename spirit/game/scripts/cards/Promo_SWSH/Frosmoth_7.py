from spirit.game.scripts.cards.SWSH1.Frosmoth_64 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=7,
    rarity=Rarities.RarePromo,
    guid='9359f1f9-7cc8-5513-bebf-fc3f5bbc211a',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH007'}

from spirit.game.scripts.cards.SWSH1.ZamazentaV_139 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=19,
    rarity=Rarities.RarePromo,
    guid='3d922d18-dcc9-590b-b9a4-6aa6f79da1b1',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH019'}

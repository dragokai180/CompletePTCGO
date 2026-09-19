from spirit.game.scripts.cards.SWSH9.CharizardVSTAR_18 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=262,
    rarity=Rarities.RarePromo,
    guid='a079770a-5d1d-5703-993b-53ac097d60fc',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH262'}

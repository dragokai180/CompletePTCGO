from spirit.game.scripts.cards.SWSH4.Snorlax_131 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=68,
    rarity=Rarities.RarePromo,
    guid='0e7f1515-cf16-53a5-973d-1f5358a11de5',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH068'}

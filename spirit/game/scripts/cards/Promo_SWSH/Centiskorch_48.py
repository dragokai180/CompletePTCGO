from spirit.game.scripts.cards.SWSH1.Centiskorch_39 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=48,
    rarity=Rarities.RarePromo,
    guid='ea741c83-927b-512b-bfd8-51a57cd91f31',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH048'}

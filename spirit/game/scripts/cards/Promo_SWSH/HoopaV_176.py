from spirit.game.scripts.cards.SWSH8.HoopaV_253 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=176,
    rarity=Rarities.RarePromo,
    guid='32f542bd-7514-5d9b-a6fb-3772afce2a57',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH176'}

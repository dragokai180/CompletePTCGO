from spirit.game.scripts.cards.SWSH7.SylveonV_74 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=202,
    rarity=Rarities.RarePromo,
    guid='e7706906-640b-5801-9c98-f5375ce65108',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH202'}

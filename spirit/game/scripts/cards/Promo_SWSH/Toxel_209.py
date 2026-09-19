from spirit.game.scripts.cards.SWSH8.Toxel_106 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=209,
    rarity=Rarities.RarePromo,
    guid='8d042775-2be4-562e-95bc-8e145cbf3501',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH209'}

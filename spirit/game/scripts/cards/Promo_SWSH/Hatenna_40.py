from spirit.game.scripts.cards.SWSH2.Hatenna_83 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=40,
    rarity=Rarities.RarePromo,
    guid='6e9182bf-51b0-5616-97c7-e25e21b99458',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH040'}

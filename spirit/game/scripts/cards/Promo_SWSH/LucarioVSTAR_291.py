from spirit.game.scripts.cards.Promo_SWSH.LucarioVSTAR_214 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=291,
    rarity=Rarities.RarePromo,
    guid='c7e45ffc-22b0-5b49-b7da-fe9c0a7e5de6',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH291'}

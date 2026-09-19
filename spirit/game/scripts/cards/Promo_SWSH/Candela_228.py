from spirit.game.scripts.cards.PGO.Candela_65 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=228,
    rarity=Rarities.RarePromo,
    guid='c5c75cb3-3c09-52de-9757-c4fa0b0967f3',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH228'}

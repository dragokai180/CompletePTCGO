from spirit.game.scripts.cards.SWSH1.ZamazentaV_139 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=77,
    rarity=Rarities.RarePromo,
    guid='427d8ddf-97f0-5f1e-a907-8c8b848eb192',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH077'}

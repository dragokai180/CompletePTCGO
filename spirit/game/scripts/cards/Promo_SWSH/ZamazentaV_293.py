from spirit.game.scripts.cards.SWSH1.ZamazentaV_139 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=293,
    rarity=Rarities.RarePromo,
    guid='681ee064-5456-56e9-8c90-8cadbada8902',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH293'}

from spirit.game.scripts.cards.SWSH35.GardevoirV_16 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=105,
    rarity=Rarities.RarePromo,
    guid='25f19154-7821-5363-a828-ca88996c24a7',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH105'}
